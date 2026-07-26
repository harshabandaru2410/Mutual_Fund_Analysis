import os
import pandas as pd

RAW_FOLDER = "data/raw"

# Find all CSV files
files = [f for f in os.listdir(RAW_FOLDER) if f.endswith(".csv")]

print(f"Found {len(files)} CSV files")

# Process every CSV file
for file in files:

    print("=" * 60)
    print(file)
    print("=" * 60)

    path = os.path.join(RAW_FOLDER, file)

    try:
        # Read CSV
        df = pd.read_csv(path)

        # Print information
        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}")
        print(e)

    print("\n")