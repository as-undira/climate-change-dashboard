from pathlib import Path
import sys
import pandas as pd

# Project Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from config import (
    RAW_DATA_FILE,
    PROCESSED_DATA_FILE,
)

# Load Dataset
df = pd.read_csv(RAW_DATA_FILE)

print("=" * 60)
print("STEP 03 - DATA PREPROCESSING")
print("=" * 60)

# hapus data duplikat
duplicate_before = df.duplicated().sum()
df = df.drop_duplicates().reset_index(drop=True)

# hapus kolom gak dipakai
columns_to_drop = [
    "timezone",
    "city_name",
    "lat",
    "lon",
    "temp_min",
    "temp_max",
    "wind_deg",
    "rain_3h",
    "rain_6h",
    "rain_12h",
    "rain_24h",
    "rain_today",
    "snow_1h",
    "snow_3h",
    "snow_6h",
    "snow_12h",
    "snow_24h",
    "snow_today",
    "weather_id",
    "weather_description",
    "weather_icon",
]

df = df.drop(columns=columns_to_drop)

# Missing Value
df["rain_1h"] = df["rain_1h"].fillna(0)

# Datetime
df["dt_iso"] = pd.to_datetime(df["dt_iso"])

# Feature Engineering
df["year"] = df["dt_iso"].dt.year

df["month"] = df["dt_iso"].dt.month

df["month_name"] = df["dt_iso"].dt.month_name()

df["day"] = df["dt_iso"].dt.day

df["hour"] = df["dt_iso"].dt.hour

df["day_name"] = df["dt_iso"].dt.day_name()

df["quarter"] = df["dt_iso"].dt.quarter

df["decade"] = (df["year"] // 10) * 10

# Sort
df = df.sort_values("dt_iso").reset_index(drop=True)

# Save Dataset
PROCESSED_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(PROCESSED_DATA_FILE, index=False)

# Summary
print(f"Duplicate Removed : {duplicate_before}")

print(f"Rows              : {df.shape[0]:,}")

print(f"Columns           : {df.shape[1]}")

print()

print("Dataset berhasil disimpan.")

print(PROCESSED_DATA_FILE)

print()

print(df.head())
