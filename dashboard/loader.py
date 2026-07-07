"""
=====================================================
File        : loader.py
Project     : Climate Change Dashboard
Description : Load processed dataset
=====================================================
"""

from pathlib import Path
import sys

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from config import PROCESSED_DATA_FILE


@st.cache_data
def load_data():

    df = pd.read_csv(PROCESSED_DATA_FILE)

    df["dt_iso"] = pd.to_datetime(df["dt_iso"])

    return df