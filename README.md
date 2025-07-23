<h1 align="left">Hi 👋! My name is Bimantyo Arya and I'm a Data Enthusiast, from Indonesia</h1>

###

<img align="right" height="150" src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjNvcDI3dnFxODNkeTZwcGlscGk3N2xzNGJ0cXpzZTM0Yzl6cjdzciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OumCa12QC9CIvBe2c1/giphy.gif"  />

###
These are my Tech Stack that i used
<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="30" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" height="30" alt="numpy logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="30" alt="pandas logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" height="30" alt="tensorflow logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height="30" alt="docker logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apache/apache-original.svg" height="30" alt="apache logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" height="30" alt="postgresql logo"  />
  <img width="12" />
</div>

###

<div align="left">
  <img src="https://img.shields.io/static/v1?message=Discord&logo=discord&label=&color=7289DA&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="discord logo"  />
  <img src="https://img.shields.io/static/v1?message=Gmail&logo=gmail&label=&color=D14836&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="gmail logo"  />
  <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="35" alt="linkedin logo"(https://www.linkedin.com/in/bimantyoarya/)  />
</div>

###


# Judul Project
Market Report on Revenue-Driving Factors in the Restaurant Industry

## Repository Outline
Project ini bertujuan untuk menganalisis faktor-faktor utama yang memengaruhi pendapatan restoran melalui proses Exploratory Data Analysis (EDA), guna menghasilkan insight bisnis dan rekomendasi strategis yang dapat mendukung pertumbuhan dan peningkatan kinerja restoran.

Sebagai bagian dari pendekatan end-to-end, saya tidak hanya berperan sebagai Data Analyst, tetapi juga mengimplementasikan peran Data Engineer. Dataset yang digunakan berasal dari Kaggle, namun dalam proyek ini saya mensimulasikan seolah-olah data tersebut diambil dari sistem database nyata untuk merefleksikan alur kerja profesional di dunia industri.

Saya menggunakan ElasticSearch sebagai sistem manajemen basis data, dan membangun proses data ingestion secara otomatis menggunakan Apache Airflow untuk mengatur dan menjadwalkan alur pengambilan data. Setelah data tersimpan dengan baik, saya melanjutkan dengan proses EDA untuk menggali pola, tren, dan insight yang dapat dijadikan dasar pengambilan keputusan bisnis.

## Problem Background
Mengutip dari Detik Bali menyatakan bahwa FnB adalah jenis usaha yang fokus di bidang makanan dan minuman, FnB merupakan salah satu jenis usaha yang paling banyak ditekuni oleh masyarakat karena memiliki potensi pasar yang paling besar. Makanan dan minuman adalah salah satu kebutuhan primer manusia. Tingginya minat terhadap segmen bisnis ini juga menjadi alasan mengapa persaingan diantara sesama pengusaha yang bergerak di bidang FnB cukup tinggi.

Mengutip dari esb.id menyatakan bahwa potensi kegagalan dalam bisnis kuliner yang berada di indonesia bisa mencapai 90% dan sejalan dengan pernyataan tersebut, The National Restaurant Association sebagai asosiasi bisnis industri restoran terkemuka di Amerika Serikat yang mewakili lebih dari 380.000 lokasi restoran memprediksi kesuksesan restoran berdasarkan data berada di angka 20%, sedangkan 60% restoran gagal pada tahun pertama sejak beroperasi, dan 80% gagal dalam rentang waktu 5 tahun sejak pembukaannya.

Bisnis FnB, termasuk restoran tergolong sangat dinamis dan bisa mengalami perubahan yang cepat dalam waktu yang relatif singkat. Maka dari itu untuk dapat membuat bisnis FnB yang bersifat long lasting perlu dilakukan optimalisasi dalam segi kualitas makanan, manajemen, service dan inovasi. Penerapan strategi bisnis yang efektif dan efisien dapat memaksimalkan potensi bisnis dan menjalankan operasional restoran yang lebih baik. Jika penerapan strategi tidak tepat, kurang efektif dan efisien dapat menimbulkan kerugian yang besar dan menimbulkan review yang kurang baik dari customer, salah satu contoh restoran yang pailit karena penerapan strategi bisnis yang tidak tepat adalah Karen’s Dinner.

## Project Output
Output dari project ini berupa sebuah dashboard sebagai market report yang berdasarkan analisa guna menghasilkan insight bisnis dan rekomendasi strategis yang dapat mendukung pertumbuhan dan kinerja restoran. Untuk output market report dapat dilihat pada folder Analysis di repository 

## Data
Sumber data yang digunakan berasal dari kaggle, untuk sumber data dapat dilihat di https://www.kaggle.com/datasets/anthonytherrien/restaurant-revenue-prediction-dataset. Dataset ini memiliki 17 kolom dan total terdapat 8368 ribu baris data. Pada dataset ini tidak ditemukan data duplicate dan missing values.  

## Method
Pada project ini melalui proses input data dari file csv ke dalam database postgreSQL yang kemudian nantinya dari postgreSQL akan dilakukan proses pengambilan data menggunakan python dan akan dilakukan preprocessing data seperti handling missing values, handling data duplicate dan kemudian akan dimasukkan ke dalam database Elasticsearch. Setelah data telah berhasil diload ke dalam Elasticsearch akan dilakukan proses visualisasi menggunakan Kibana yang nantinya akan menghasilkan market report berbasis visual.

## Stacks
Untuk library yang digunakan pada project ini adalah penggunaan database postgreSQL, bahasa pemrograman python, numpy, pandas, database Elasticsearch, dan airflow

## Reference
Referensi landasan untuk project ini : 

- https://www.detik.com/bali/berita/d-6560178/fnb-adalah-pengertian-fungsi-pembagian-departemen-dan-peluang-bisnisnya

- https://www.esb.id/id/inspirasi/5-strategi-kelola-restoran-yang-efektif-dan-efisien

---

