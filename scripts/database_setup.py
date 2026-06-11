import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

# query = """
# SELECT DISTINCT fund_house
# FROM dim_fund;
# """

# # 3. Use Pandas to run the query and display the results
# df = pd.read_sql(query, engine)
# print(df.head())
nav_history = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded")
query = """
SELECT COUNT(*)
FROM fact_nav
"""

df = pd.read_sql(query, engine)

print(df)