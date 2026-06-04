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

# fund_master = pd.read_csv("data/raw/01_fund_master.csv")

# print("Fund Houses:")
# print(fund_master["fund_house"].unique())

# print("\nCategories:")
# print(fund_master["category"].unique())

# print("\nSub Categories:")
# print(fund_master["sub_category"].unique())

# print("\nRisk Grades:")
# print(fund_master["risk_category"].unique())



# fund_master = pd.read_csv("data/raw/01_fund_master.csv")
# nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# fund_codes = set(fund_master["amfi_code"])
# nav_codes = set(nav_history["amfi_code"])

# missing_codes = fund_codes - nav_codes

# print("Missing Codes:", len(missing_codes))
# print(missing_codes)