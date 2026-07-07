"""
=====================================================
File        : insights.py
Project     : Dashboard Perubahan Iklim
Description : Analisis Iklim Jangka Panjang
Author      : Agung Sudarto
=====================================================
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# =====================================================
# DISTRIBUSI KONDISI CUACA
# =====================================================

def weather_distribution(df: pd.DataFrame):

    data = (
        df["weather_main"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
        .reset_index()
    )

    data.columns = [
        "Kondisi Cuaca",
        "Persentase",
    ]

    utama = data[
        data["Persentase"] >= 1
    ].copy()

    lainnya = data[
        data["Persentase"] < 1
    ]["Persentase"].sum()

    if lainnya > 0:

        utama.loc[len(utama)] = [

            "Lainnya",

            round(lainnya, 2)

        ]

    utama["Legenda"] = (

        utama["Kondisi Cuaca"]

        + " ("

        + utama["Persentase"].astype(str)

        + "%)"

    )

    fig = px.pie(

        utama,

        names="Legenda",

        values="Persentase",

        hole=0.60,

    )

    fig.update_traces(

        textinfo="none",

        hovertemplate="<b>%{label}</b><br>%{percent}<extra></extra>",

    )

    fig.update_layout(

        title="Distribusi Kondisi Cuaca",

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=540,

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20,

        ),

        legend=dict(

            orientation="v",

            y=0.5,

            yanchor="middle",

            x=1.02,

        ),

    )

    with st.container(border=True):

        st.plotly_chart(

            fig,

            use_container_width=True,

            config={

                "displaylogo": False,

            },

        )


# =====================================================
# KORELASI ANTAR VARIABEL
# =====================================================

def correlation_heatmap(df: pd.DataFrame):

    corr = df[
        [
            "temp",
            "humidity",
            "pressure",
            "wind_speed",
            "rain_1h",
            "clouds_all",
        ]
    ].corr()

    corr.index = [

        "Suhu",

        "Kelembapan",

        "Tekanan",

        "Kecepatan Angin",

        "Curah Hujan",

        "Tutupan Awan",

    ]

    corr.columns = corr.index

    fig = px.imshow(

        corr,

        text_auto=".2f",

        aspect="auto",

        color_continuous_scale="RdBu_r",

    )

    fig.update_layout(

        title="Korelasi Antar Variabel",

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=540,

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20,

        ),

    )

    with st.container(border=True):

        st.plotly_chart(

            fig,

            use_container_width=True,

            config={

                "displaylogo": False,

            },

        )


# =====================================================
# POLA SUHU BULANAN
# =====================================================

def monthly_heatmap(df: pd.DataFrame):

    data = (

        df.groupby(

            [

                "year",

                "month",

            ]

        )["temp"]

        .mean()

        .reset_index()

    )

    pivot = data.pivot(

        index="year",

        columns="month",

        values="temp",

    )

    pivot.columns = [

        "Jan",

        "Feb",

        "Mar",

        "Apr",

        "Mei",

        "Jun",

        "Jul",

        "Agu",

        "Sep",

        "Okt",

        "Nov",

        "Des",

    ]

    fig = go.Figure(

        data=go.Heatmap(

            z=pivot.values,

            x=pivot.columns,

            y=pivot.index,

            colorscale="YlOrRd",

            colorbar=dict(

                title="°C"

            )

        )

    )

    fig.update_layout(

        title="Pola Suhu Bulanan",

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=620,

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20,

        ),

    )

    with st.container(border=True):

        st.plotly_chart(

            fig,

            use_container_width=True,

            config={

                "displaylogo": False,

            },

        )
        
# =====================================================
# KEJADIAN IKLIM EKSTREM
# =====================================================

def extreme_climate_events(df: pd.DataFrame):

    col1, col2 = st.columns(2)

    # =====================================================
    # SUHU TERTINGGI
    # =====================================================

    with col1:

        st.subheader("Suhu Tertinggi")

        highest_temp = (

            df.nlargest(10, "temp")[

                [

                    "dt_iso",

                    "temp",

                    "humidity",

                    "weather_main",

                ]

            ]

            .rename(

                columns={

                    "dt_iso": "Tanggal",

                    "temp": "Suhu (°C)",

                    "humidity": "Kelembapan (%)",

                    "weather_main": "Kondisi Cuaca",

                }

            )

        )

        highest_temp["Tanggal"] = (

            pd.to_datetime(

                highest_temp["Tanggal"]

            ).dt.strftime("%d-%m-%Y")

        )

        highest_temp["Suhu (°C)"] = (

            highest_temp["Suhu (°C)"]

            .round(2)

        )

        highest_temp["Kelembapan (%)"] = (

            highest_temp["Kelembapan (%)"]

            .round(2)

        )

        with st.container(border=True):

            st.dataframe(

                highest_temp,

                use_container_width=True,

                hide_index=True,

            )

    # =====================================================
    # CURAH HUJAN TERTINGGI
    # =====================================================

    with col2:

        st.subheader("Curah Hujan Tertinggi")

        highest_rain = (

            df.nlargest(10, "rain_1h")[

                [

                    "dt_iso",

                    "rain_1h",

                    "weather_main",

                ]

            ]

            .rename(

                columns={

                    "dt_iso": "Tanggal",

                    "rain_1h": "Curah Hujan (mm)",

                    "weather_main": "Kondisi Cuaca",

                }

            )

        )

        highest_rain["Tanggal"] = (

            pd.to_datetime(

                highest_rain["Tanggal"]

            ).dt.strftime("%d-%m-%Y")

        )

        highest_rain["Curah Hujan (mm)"] = (

            highest_rain["Curah Hujan (mm)"]

            .round(2)

        )

        with st.container(border=True):

            st.dataframe(

                highest_rain,

                use_container_width=True,

                hide_index=True,

            )


# =====================================================
# SECTION ANALISIS IKLIM
# =====================================================

def climate_insights(df: pd.DataFrame):

    st.header("Analisis Iklim 30 Tahun")

    st.caption(

        "Visualisasi pada bagian ini menggunakan seluruh data periode 1990–2020 sehingga tidak dipengaruhi oleh filter tanggal."

    )

    # =====================================================
    # BARIS 1
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        weather_distribution(df)

    with col2:

        correlation_heatmap(df)

    # =====================================================
    # BARIS 2
    # =====================================================

    monthly_heatmap(df)

    st.write("")

    # =====================================================
    # BARIS 3
    # =====================================================

    extreme_climate_events(df)


# =====================================================
# EXPORT
# =====================================================

__all__ = [

    "weather_distribution",

    "correlation_heatmap",

    "monthly_heatmap",

    "extreme_climate_events",

    "climate_insights",

]