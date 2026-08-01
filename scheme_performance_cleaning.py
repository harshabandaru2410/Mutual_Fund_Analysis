import pandas as pd
import os

# =====================================================
# Folder Paths
# =====================================================

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

# =====================================================
# Read Dataset
# =====================================================

performance = pd.read_csv(
    os.path.join(
        RAW_FOLDER,
        "07_scheme_performance.csv"
    )
)

# =====================================================
# Dataset Information
# =====================================================

print("=" * 70)
print("SCHEME PERFORMANCE DATASET")
print("=" * 70)

print("\nColumns:")
print(performance.columns.tolist())

print("\nFirst 5 Rows:")
print(performance.head())

print("\nShape:")
print(performance.shape)

print("\nData Types:")
print(performance.dtypes)

print("\nMissing Values:")
print(performance.isnull().sum())

print("\nDuplicate Rows:")
print(performance.duplicated().sum())

# =====================================================
# Validate Return Columns
# =====================================================

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

print("\n" + "=" * 70)
print("VALIDATING RETURN COLUMNS")
print("=" * 70)

for column in return_columns:

    # Convert to numeric
    performance[column] = pd.to_numeric(
        performance[column],
        errors="coerce"
    )

    print(f"\nColumn : {column}")
    print("Missing Values :", performance[column].isnull().sum())
    print("Minimum Value :", performance[column].min())
    print("Maximum Value :", performance[column].max())

# =====================================================
# Flag Return Anomalies
# =====================================================

print("\n" + "=" * 70)
print("RETURN VALUE ANOMALIES")
print("=" * 70)

for column in return_columns:

    anomalies = performance[
        (performance[column] < -100) |
        (performance[column] > 100)
    ]

    print(f"\nChecking {column}")

    if len(anomalies) == 0:
        print("No anomalies found.")

    else:
        print(anomalies[
            [
                "amfi_code",
                "scheme_name",
                column
            ]
        ])

# =====================================================
# Validate Expense Ratio
# =====================================================

print("\n" + "=" * 70)
print("EXPENSE RATIO VALIDATION")
print("=" * 70)

invalid_expense = performance[
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratio Records :", len(invalid_expense))

if len(invalid_expense) > 0:

    print(invalid_expense[
        [
            "amfi_code",
            "scheme_name",
            "expense_ratio_pct"
        ]
    ])

else:

    print("All expense ratios are within the valid range.")

# =====================================================
# Remove Duplicate Rows
# =====================================================

performance = performance.drop_duplicates()

print("\nDuplicate Rows After Cleaning")
print(performance.duplicated().sum())

# =====================================================
# Save Cleaned Dataset
# =====================================================

performance.to_csv(
    os.path.join(
        PROCESSED_FOLDER,
        "07_scheme_performance.csv"
    ),
    index=False
)

print("\nCleaned scheme_performance.csv saved successfully!")