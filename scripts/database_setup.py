import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

performance = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

query = """
SELECT
    fund_house,
    AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance
GROUP BY fund_house;
"""

df = pd.read_sql(query, engine)

print(df)