"""
=====================================================
File        : charts.py
Project     : Dashboard Perubahan Iklim
Description : Grafik Tren Iklim Dinamis
Author      : Agung Sudarto
=====================================================
"""

import pandas as pd
import plotly.express as px
import streamlit as st

# =====================================================
# WARNA GRAFIK
# =====================================================

CHART_COLORS = {

    "Suhu": "#E53935",

    "Kelembapan": "#1E88E5",

    "Tekanan Udara": "#FB8C00",

    "Kecepatan Angin": "#43A047",

    "Curah Hujan": "#1565C0",

    "Tutupan Awan": "#757575",

}

# =====================================================
# KONFIGURASI GRAFIK
# =====================================================

CHART_CONFIG = {

    "Suhu": {

        "column": "temp",

        "title": "Tren Suhu",

        "ylabel": "Suhu (°C)",

        "aggregation": "mean",

    },

    "Kelembapan": {

        "column": "humidity",

        "title": "Tren Kelembapan",

        "ylabel": "Kelembapan (%)",

        "aggregation": "mean",

    },

    "Tekanan Udara": {

        "column": "pressure",

        "title": "Tren Tekanan Udara",

        "ylabel": "Tekanan Udara (hPa)",

        "aggregation": "mean",

    },

    "Kecepatan Angin": {

        "column": "wind_speed",

        "title": "Tren Kecepatan Angin",

        "ylabel": "Kecepatan Angin (m/s)",

        "aggregation": "mean",

    },

    "Curah Hujan": {

        "column": "rain_1h",

        "title": "Tren Curah Hujan",

        "ylabel": "Curah Hujan (mm)",

        "aggregation": "sum",

    },

    "Tutupan Awan": {

        "column": "clouds_all",

        "title": "Tren Tutupan Awan",

        "ylabel": "Tutupan Awan (%)",

        "aggregation": "mean",

    },

}

# =====================================================
# AGREGASI DATA
# =====================================================

def aggregate_data(df, column, aggregation):

    data = df.copy()

    start_date = data["dt_iso"].min()

    end_date = data["dt_iso"].max()

    total_days = (end_date - start_date).days

    # ---------------------------------------------

    if total_days <= 31:

        data["group"] = data["dt_iso"]

        group_column = "group"

        period_name = "Per Jam"

    elif total_days <= 365:

        data["group"] = data["dt_iso"].dt.date

        group_column = "group"

        period_name = "Per Hari"

    elif total_days <= 365 * 5:

        data["group"] = (

            data["dt_iso"]

            .dt.to_period("M")

            .astype(str)

        )

        group_column = "group"

        period_name = "Per Bulan"

    else:

        group_column = "year"

        period_name = "Per Tahun"

    # ---------------------------------------------

    if aggregation == "mean":

        result = (

            data

            .groupby(group_column, as_index=False)[column]

            .mean()

        )

    else:

        result = (

            data

            .groupby(group_column, as_index=False)[column]

            .sum()

        )

    return result, group_column, period_name

# =====================================================
# MEMBUAT GRAFIK
# =====================================================

def create_line_chart(

    df,

    title,

    x_column,

    y_column,

    y_title,

    color,

):

    fig = px.line(

        df,

        x=x_column,

        y=y_column,

        markers=True,

    )

    fig.update_traces(

        line=dict(

            color=color,

            width=3,

        ),

        marker=dict(

            color=color,

            size=7,

            line=dict(

                color="white",

                width=1,

            ),

        ),

        hovertemplate="<b>%{x}</b><br>%{y:.2f}<extra></extra>",

    )

    fig.update_layout(

        template="plotly_white",

        height=500,

        paper_bgcolor="white",

        plot_bgcolor="white",

        margin=dict(

            l=20,

            r=20,

            t=65,

            b=20,

        ),

        title=dict(

            text=title,

            x=0,

            xanchor="left",

            font=dict(

                size=22,

                color="#111827",

            ),

        ),

        xaxis=dict(

            title="Periode",

            showgrid=False,

            showline=True,

            linewidth=1,

            linecolor="#D1D5DB",

            mirror=True,

        ),

        yaxis=dict(

            title=y_title,

            showgrid=True,

            gridcolor="#E5E7EB",

            showline=True,

            linewidth=1,

            linecolor="#D1D5DB",

            mirror=True,

        ),

        hovermode="x unified",

        showlegend=False,

    )

    return fig

# =====================================================
# MENAMPILKAN GRAFIK
# =====================================================

def show_trend_chart(
    df: pd.DataFrame,
    selected_variable: str
):

    config = CHART_CONFIG[selected_variable]

    chart_data, x_column, aggregation_name = aggregate_data(

        df=df,

        column=config["column"],

        aggregation=config["aggregation"]

    )

    st.caption(

        f"Agregasi Data : **{aggregation_name}**"

    )

    fig = create_line_chart(

        df=chart_data,

        title=config["title"],

        x_column=x_column,

        y_column=config["column"],

        y_title=config["ylabel"],

        color=CHART_COLORS[selected_variable],

    )

    with st.container(border=True):

        st.plotly_chart(

            fig,

            use_container_width=True,

            config={

                "displaylogo": False,

                "responsive": True,

                "scrollZoom": False,

                "modeBarButtonsToRemove": [

                    "lasso2d",

                    "select2d",

                    "autoScale2d",

                    "zoom2d",

                    "pan2d",

                    "resetScale2d",

                ],

            },

        )


# =====================================================
# PILIH VARIABEL
# =====================================================

def variable_selector():

    return st.segmented_control(

        label="Variabel Iklim",

        options=list(CHART_CONFIG.keys()),

        default="Suhu",

        selection_mode="single",

        width="stretch",

    )


# =====================================================
# SECTION EKSPLORASI
# =====================================================

def exploratory_section(df):

    st.subheader("Tren Iklim")

    selected_variable = variable_selector()

    st.write("")

    show_trend_chart(

        df=df,

        selected_variable=selected_variable,

    )


# =====================================================
# EXPORT
# =====================================================

__all__ = [

    "exploratory_section",

    "show_trend_chart",

    "variable_selector",

]