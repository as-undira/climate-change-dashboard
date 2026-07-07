from pathlib import Path
import sys
import pandas as pd

# Tambahkan root project ke Python Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(str(PROJECT_ROOT))

from config import RAW_DATA_FILE


# Function
def load_dataset():
    """
    Membaca dataset dari file CSV.

    Returns
    -------
    pandas.DataFrame
        Dataset cuaca Denpasar.
    """

    if not RAW_DATA_FILE.exists():

        raise FileNotFoundError(f"Dataset tidak ditemukan:\n{RAW_DATA_FILE}")

    df = pd.read_csv(RAW_DATA_FILE)

    return df


# Main
if __name__ == "__main__":

    print("=" * 60)
    print("CLIMATE CHANGE DASHBOARD")
    print("STEP 01 - EXTRACT DATASET")
    print("=" * 60)

    df = load_dataset()

    print()

    print("Dataset berhasil dibaca.")

    print(f"Jumlah Baris : {df.shape[0]:,}")

    print(f"Jumlah Kolom : {df.shape[1]}")

    print()

    print(df.head())
