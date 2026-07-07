from pathlib import Path
import sys
import pandas as pd

# Project Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from config import PROCESSED_DATA_FILE

# Load Dataset
df = pd.read_csv(PROCESSED_DATA_FILE)

print("=" * 60)
print("STEP 04 - ANALYTICS")
print("=" * 60)

print(f"Jumlah Data : {len(df):,}")
print(f"Jumlah Kolom: {len(df.columns)}")

print()

print("=" * 60)
print("PERIODE DATA")
print("=" * 60)

print("Mulai :", df["dt_iso"].min())
print("Sampai:", df["dt_iso"].max())

print()

print("=" * 60)
print("RATA-RATA")
print("=" * 60)

print(f"Suhu       : {df['temp'].mean():.2f} °C")
print(f"Kelembapan : {df['humidity'].mean():.2f} %")
print(f"Tekanan    : {df['pressure'].mean():.2f} hPa")
print(f"Angin      : {df['wind_speed'].mean():.2f} m/s")
print(f"Tutupan Awan : {df['clouds_all'].mean():.2f} %")
print(f"Total Hujan  : {df['rain_1h'].sum():.2f} mm")

print()

print("=" * 60)
print("WEATHER")
print("=" * 60)

print(df["weather_main"].value_counts())

print()

print("=" * 60)
print("YEAR RANGE")
print("=" * 60)

print(df["year"].min(), "-", df["year"].max())

print()

print("Analytics selesai.")
