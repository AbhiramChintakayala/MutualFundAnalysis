import pandas as pd

transactions = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print(
    transactions["kyc_status"].unique()
)
transactions = (
    transactions.drop_duplicates()
)
transactions.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("Investor transactions cleaned!")