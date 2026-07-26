import pandas as pd
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
print("NAV History Columns:")
print(nav_history.columns.tolist())
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])
missing_codes = fund_codes - nav_codes  
print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

print(f"Total Fund Master Codes : {len(fund_codes)}")
print(f"Total NAV History Codes : {len(nav_codes)}")

print(f"Missing Codes : {len(missing_codes)}")

if len(missing_codes) == 0:
    print("All AMFI codes are present.")
else:
    print("Missing AMFI Codes:")
    print(sorted(missing_codes))