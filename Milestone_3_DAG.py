"""
=================================================

MILESTONE 3 

- Nama  : Bimantyo Arya Majid

- Objective : Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch. Dataset yang akan digunakan adalah mengenai Restaurant Revenue Prediction 

=================================================
"""

# Import Libaries
import pandas as pd  # Untuk manipulasi dan analisis data
import datetime as dt  # Untuk manajemen waktu dan tanggal secara umum
from datetime import timedelta  # Untuk menentukan jeda waktu seperti retry_delay, interval, dsb
from airflow import DAG  # Sebagai struktur utama yang mendefinisikan alur kerja di Airflow
from airflow.decorators import task  # Untuk membuat task di Airflow menggunakan decorator Python modern (@task)
from airflow.operators.empty import EmptyOperator  # Operator dummy yang sering digunakan sebagai titik awal atau akhir (start/end node) dalam DAG
from elasticsearch import Elasticsearch  # Untuk berinteraksi dengan Elasticsearch
from sqlalchemy import create_engine  # Untuk membuat koneksi ke database SQL 

default_args= {
    'owner': 'bima',
    'start_date': dt.datetime(2024, 11, 1) - timedelta(hours=7),
    'retry':1,
    'retry_delay': timedelta(seconds=30),
}

with DAG(
    'milestone3_final',
    description='proses etl data warehouse dari postgres ke airflow',
    schedule_interval='10-30/10 9 * * 6', # Program dijalankan setiap hari sabtu dari jam 9.10 - 9.30 dengan interval 10 menit 
    default_args=default_args,
    catchup = False
    ) as dag:

    # Operator kosong pembuka
    start = EmptyOperator(task_id='start')

    @task()
    def fetch_from_postgresql():
        """
        Fungsi ini bertujuan untuk mengambil data dari tabel 'table_m3' di PostgreSQL dan 
        Mengambil seluruh data dari tabel 'table_m3' di PostgreSQL
        dan menyimpannya ke dalam file CSV sementara.
        """
        # Mendefinisikan USER
        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"
        
        # Koneksi database
        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"
        engine = create_engine(postgres_url)
        conn = engine.connect()
        
        # Mengambil data dari postgreSQL
        df=pd.read_sql(f"SELECT * FROM table_m3", conn)

        # Menyimpan data ke dalam csv 
        df.to_csv('/opt/airflow/data/P2M3_Bimantyo_arya_data_raw.csv',index=False)
        print('Extracting Data dari Postgre telah berhasil')

    @task()
    def preprocess_data():
        """
        Fungsi ini bertujuan untuk melakuan preprocessing terhadap data file CSV yang telah didapatkan dengan melakukan 
        melakukan drop terhadap data yang duplikat duplikat, kemudian mengubah nama column menjadi huruf lowercase dan 
        menghilangkan spasi, kemduian mengubah data type 'Parking Availability' dari Yes/No ke Boolean dan yang terakhir
        melakukan imputasi jika terdapat data null value 
        Hasilnya disimpan sebagai 'clean_data.csv'.
        """
     
        # Data loading
        df = pd.read_csv("/opt/airflow/data/P2M3_Bimantyo_arya_data_raw.csv")
        
         # Menghapus semua data yang berpotensi duplikat 
        df.drop_duplicates(inplace=True)
        
        # Mengubah nama column agar memiliki huruf yang sama rata dan mengubah spasi menjadi menjadi '_'
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

        # Mengubah data type Parking Availability 
        df['parking_availability'] = df['parking_availability'].map({'Yes': True, 'No': False})
        
        # Melakukan handle missing values 
        df.fillna(df.mean(numeric_only=True), inplace=True)
        
        # Menyimpan data clean ke dalam csv 
        df.to_csv('/opt/airflow/data/P2M3_Bimantyo_arya_data_clean.csv',index=False)
        print('Preprocessed data telah berhasil')

    @task()
    def load_to_elastic():
        """
        Fungsi ini bertujuan untuk melakuan load data yang sudah dilakukan preprocessing dan berbentuk .CSV ke dalam
        database Elasticsearch yang nantinya akan dilakukan visualisasi menggunakan Kibana.
        """
        # Data loading
        df = pd.read_csv("/opt/airflow/data/P2M3_Bimantyo_arya_data_clean.csv")
        
        # Koneksi ke airflow ke elasticsearch
        es = Elasticsearch("http://elasticsearch:9200")
        
        # Melakukan cek koneksi
        print(es.ping())
        
        # Looping mengirim data json ke elasticsearch
        for i, row in df.iterrows():
            doc = row.to_json()
            res = es.index(index="milestone3_final", body=doc, id=i)
        print("-------Post to ElasticSearch is Succes------")
    
    # Operator kosong penutup
    end = EmptyOperator(task_id='end')
    
    # Urutan penjadwalan
    start >> fetch_from_postgresql() >> preprocess_data() >> load_to_elastic() >> end