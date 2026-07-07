"""
=====================================================
File        : metrics.py
Project     : Dashboard Perubahan Iklim
Description : KPI Dashboard
Author      : Agung Sudarto
=====================================================
"""

import streamlit as st


# =====================================================
# KOMPONEN KPI
# =====================================================

def metric_card(title, value):

    with st.container(border=True):

        st.markdown(
            f"""
<div class="metric-card">
    <div class="metric-title">{title}</div>
    <div class="metric-value">{value}</div>
</div>
""",
            unsafe_allow_html=True,
        )


# =====================================================
# MENAMPILKAN KPI
# =====================================================

def show_metrics(df):

    col1, col2, col3 = st.columns(3)

    with col1:

        metric_card(

            "Rata-rata Suhu",

            f"{df['temp'].mean():.2f} °C"

        )

    with col2:

        metric_card(

            "Rata-rata Kelembapan",

            f"{df['humidity'].mean():.2f} %"

        )

    with col3:

        metric_card(

            "Rata-rata Tekanan Udara",

            f"{df['pressure'].mean():.2f} hPa"

        )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        metric_card(

            "Rata-rata Tutupan Awan",

            f"{df['clouds_all'].mean():.2f} %"

        )

    with col2:

        metric_card(

            "Rata-rata Kecepatan Angin",

            f"{df['wind_speed'].mean():.2f} m/s"

        )

    with col3:

        metric_card(

            "Total Curah Hujan",

            f"{df['rain_1h'].sum():,.2f} mm"

        )


# =====================================================
# EXPORT
# =====================================================

__all__ = [

    "show_metrics",

]