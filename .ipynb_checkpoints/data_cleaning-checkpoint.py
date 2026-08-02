import pandas as pd
import os
RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"
nav=pd.read_csv(os.path.join(RAW_FOLDER,"02_nav_history.csv"))

print("\nFirst 5 Rows")
print(nav.head())

print("\nShape")
print(nav.shape)

print("\nData Types")
print(nav.dtypes)

print("\nMissing values")
print(nav.isnull().sum())

print("\nDuplicate Rows")
print(nav.duplicated().sum())

nav["date"]=pd.to_datetime(nav["date"])
print("\nData Types After Date Conversion")
print(nav.dtypes)

nav= nav.sort_values(by=["amfi_code","date"])
print("\nAfter Sorting")
print(nav.head())

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

print("\nMissing Values After Forward Fill")
print(nav["nav"].isnull().sum())
nav=nav.drop_duplicates()
print("\nDuplicate Rows After Cleaning")
print(nav.duplicated().sum())

invalid_nav=nav[nav["nav"]<=0]
print("\nInvalid nav records")
print(invalid_nav)

nav = nav[nav["nav"] > 0]
print(nav)
print("\n minimum nav value")
print(nav["nav"].min())

#saving the cleaned data set
nav.to_csv(os.path.join(PROCESSED_FOLDER,"02_nav_history.csv"),index=False)
print("\nCleaned nav_history.csv saved successfully")