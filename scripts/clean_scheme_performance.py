import pandas as pd

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)
anomalies = performance[
    (performance["expense_ratio"] < 0.1)
    |
    (performance["expense_ratio"] > 2.5)
]

print(anomalies)

performance.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Scheme performance cleaned!")
