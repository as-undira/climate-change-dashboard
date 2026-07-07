"""
=====================================================
File        : 02_data_audit.py
Project     : Climate Change Dashboard
Description : Audit dataset
=====================================================
"""

from pathlib import Path
import sys

import pandas as pd

# =====================================================
# Project Path
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from config import RAW_DATA_FILE

# =====================================================
# Load Dataset
# =====================================================

df = pd.read_csv(RAW_DATA_FILE)

# =====================================================
# Audit
# =====================================================

print("=" * 60)
print("DATASET AUDIT")
print("=" * 60)

print(f"Rows             : {df.shape[0]:,}")
print(f"Columns          : {df.shape[1]}")
print(f"Duplicate Rows   : {df.duplicated().sum()}")
print()

print("=" * 60)
print("COLUMN INFORMATION")
print("=" * 60)

info = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Missing": df.isnull().sum().values,
    "Non Missing": df.notnull().sum().values
})

print(info)

print()

print("=" * 60)
print("NUMERIC STATISTICS")
print("=" * 60)

print(df.describe())

print()

print("=" * 60)
print("MEMORY USAGE")
print("=" * 60)

memory = df.memory_usage(deep=True).sum() / 1024**2
print(f"{memory:.2f} MB")