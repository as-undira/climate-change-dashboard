import streamlit as st

from dashboard.loader import load_data
from dashboard.theme import load_theme
from dashboard.metrics import show_metrics
from dashboard.charts import exploratory_section
from dashboard.insights import climate_insights

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Dashboard Perubahan Iklim",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# LOAD THEME
load_theme()

# LOAD DATA
df = load_data()

# HEADER
st.title("Dashboard Perubahan Iklim")

st.markdown("""
### Visualisasi Tren Perubahan Iklim Menggunakan Data Lingkungan Multi-Dekade

Dashboard ini menyajikan analisis perubahan iklim Kota Denpasar menggunakan data cuaca historis periode **1990–2020**.
""")

st.divider()

# FILTER DATA
st.header("Eksplorasi Data Iklim")

with st.container(border=True):
    col1, col2, col3 = st.columns([1, 1, 0.6])
    with col1:
        start_date = st.date_input(
            "Tanggal Awal",
            value=df["dt_iso"].min().date(),
            min_value=df["dt_iso"].min().date(),
            max_value=df["dt_iso"].max().date(),
        )

    with col2:
        end_date = st.date_input(
            "Tanggal Akhir",
            value=df["dt_iso"].max().date(),
            min_value=df["dt_iso"].min().date(),
            max_value=df["dt_iso"].max().date(),
        )

    with col3:
        st.write("")
        st.write("")

        reset = st.button(
            "Atur Ulang",
            use_container_width=True,
        )

if reset:
    start_date = df["dt_iso"].min().date()
    end_date = df["dt_iso"].max().date()

filtered_df = df[
    (df["dt_iso"].dt.date >= start_date) & (df["dt_iso"].dt.date <= end_date)
].copy()

st.divider()

# KPI
show_metrics(filtered_df)

st.divider()

# TREN IKLIM
exploratory_section(filtered_df)

st.divider()

# ANALISIS IKLIM
climate_insights(df)

st.divider()

# FOOTER
st.markdown(
    """
<div style="text-align:center;color:#6B7280;font-size:14px;padding:10px 0">

Dashboard Perubahan Iklim Kota Denpasar (1990–2020)<br>

Tugas Besar Analitik dan Visualisasi Data

</div>
""",
    unsafe_allow_html=True,
)
