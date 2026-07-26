import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 80)
print("FUND MASTER DATASET EXPLORATION")
print("=" * 80)

# Basic Information
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\n" + "=" * 80)
print("UNIQUE VALUES IN EACH COLUMN")
print("=" * 80)

# Print unique values for every column
for column in df.columns:
    print(f"\nColumn: {column}")
    unique_values = df[column].dropna().unique()
    print(f"Total Unique Values: {len(unique_values)}")

    # Show first 20 unique values only
    if len(unique_values) > 20:
        print(unique_values[:20])
        print("...")
    else:
        print(unique_values)

print("\n" + "=" * 80)
print("SCHEME CODE SAMPLE")
print("=" * 80)

# Find the scheme code column automatically
scheme_columns = [col for col in df.columns if "scheme" in col.lower() and "code" in col.lower()]

if scheme_columns:
    scheme_col = scheme_columns[0]
    print(f"Detected Scheme Code Column: {scheme_col}")
    print(df[scheme_col].head(10))
else:
    print("Scheme code column not found automatically.")