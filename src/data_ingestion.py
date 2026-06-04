import pandas as pd
import os

data_folder = "data/raw"

csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

for file in csv_files:

    print("\n" + "="*70)
    print(f"DATASET: {file}")
    print("="*70)

    path = os.path.join(data_folder, file)

    df = pd.read_csv(path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Rows:")
    print(df.head())