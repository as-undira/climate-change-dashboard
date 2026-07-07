"""
=====================================================
File        : config.py
Project     : Climate Change Dashboard
Description : Konfigurasi utama project
Author      : Agung Sudarto
=====================================================
"""

from pathlib import Path

# =====================================================
# ROOT DIRECTORY
# =====================================================

ROOT_DIR = Path(__file__).resolve().parent

# =====================================================
# DATA DIRECTORY
# =====================================================

DATA_DIR = ROOT_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

# =====================================================
# DATA FILE
# =====================================================

RAW_DATA_FILE = RAW_DATA_DIR / "openweatherdata-denpasar-1990-2020v0.1.csv"

PROCESSED_DATA_FILE = PROCESSED_DATA_DIR / "climate_clean.csv"