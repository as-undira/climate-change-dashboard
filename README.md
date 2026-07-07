# Dashboard Perubahan Iklim
Dashboard interaktif berbasis **Streamlit** untuk menganalisis perubahan iklim Kota Denpasar menggunakan data cuaca historis periode **1990–2020**. Dashboard ini dikembangkan sebagai implementasi analitik data dan visualisasi untuk membantu memahami tren iklim jangka panjang melalui berbagai visualisasi interaktif.

---

## Tentang Proyek
Perubahan iklim merupakan salah satu isu global yang berdampak pada berbagai aspek kehidupan. Melalui dashboard ini, pengguna dapat mengeksplorasi data cuaca historis Kota Denpasar, melihat tren perubahan variabel iklim, serta memperoleh insight dari visualisasi statistik yang dihasilkan.

Dashboard ini dibangun menggunakan Python dan Streamlit dengan pendekatan ETL (Extract, Transform, Load) sehingga seluruh proses mulai dari pengolahan data hingga visualisasi dilakukan secara sistematis.


## Tujuan
- Menampilkan tren perubahan iklim Kota Denpasar.
- Menyediakan visualisasi interaktif untuk eksplorasi data.
- Menampilkan insight iklim jangka panjang berdasarkan data historis.
- Mendukung proses analisis data menggunakan dashboard yang mudah dipahami.


## Teknologi
- Python
- Streamlit
- Pandas
- Plotly
- NumPy


## Struktur Project
CLIMATEDENPASAR/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── dashboard/
│   ├── charts.py
│   ├── insights.py
│   ├── loader.py
│   ├── metrics.py
│   └── theme.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── etl/
│   ├── 01_extract.py
│   ├── 02_data_audit.py
│   ├── 03_preprocessing.py
│   └── 04_analytics.py


## Instalasi
Clone repository
```bash
git clone https://github.com/as-undira/climate-change-dashboard
```

Masuk ke folder project
```bash
cd climate-change-dashboard
```

Install seluruh dependency
```bash
pip install -r requirements.txt
```

Jalankan aplikasi
```bash
streamlit run app.py
```


## 📊 Dataset
Dataset yang digunakan merupakan data cuaca historis Kota Denpasar periode 1990–2020 yang berisi berbagai parameter iklim seperti:
- Temperatur
- Kelembapan
- Tekanan Udara
- Kecepatan Angin
- Curah Hujan
- Tutupan Awan
- Kondisi Cuaca


## 👨‍💻 Pengembang
Agung Sudartono


## 📄 Lisensi
Project ini dikembangkan untuk keperluan akademik sebagai Tugas Besar Mata Kuliah Analitik dan Visualisasi Data.
Data source from Kaggle https://www.kaggle.com/datasets/cornflake15/denpasarbalihistoricalweatherdata