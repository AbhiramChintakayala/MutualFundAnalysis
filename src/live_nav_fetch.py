# import requests
# import pandas as pd

# schemes = {
#     "SBI_Bluechip": 119551,
#     "ICICI_Bluechip": 120503,
#     "Nippon_Large_Cap": 118632,
#     "Axis_Bluechip": 119092,
#     "Kotak_Bluechip": 120841
# }

# for fund_name, scheme_code in schemes.items():

#     url = f"https://api.mfapi.in/mf/{scheme_code}"

#     response = requests.get(url)

#     data = response.json()

#     nav_df = pd.DataFrame(data['data'])

#     filename = f"data/raw/{fund_name}.csv"

#     nav_df.to_csv(filename, index=False)

#     print(f"{fund_name} saved successfully")
import pandas as pd

# fund_master = pd.read_csv("data/raw/01_fund_master.csv")

# print("Fund Houses:")
# print(fund_master["fund_house"].unique())

# print("\nCategories:")
# print(fund_master["category"].unique())

# print("\nSub Categories:")
# print(fund_master["sub_category"].unique())

# print("\nRisk Grades:")
# print(fund_master["risk_category"].unique())
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print("Missing Codes:", len(missing_codes))
print(missing_codes)
