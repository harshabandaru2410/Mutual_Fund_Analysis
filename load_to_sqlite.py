import pandas as pd
from sqlalchemy import create_engine

# ======================================================
# CREATE SQLITE DATABASE CONNECTION
# ======================================================

engine = create_engine("sqlite:///bluestock_mf.db")

print("=" * 60)
print("CONNECTED TO SQLITE DATABASE")
print("=" * 60)

# ======================================================
# LOAD DIM_FUND
# ======================================================

fund = pd.read_csv("data/raw/01_fund_master.csv")

dim_fund = fund[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "sub_category",
        "plan",
        "fund_manager",
        "risk_category",
    ]
]

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False,
)

print("dim_fund loaded successfully!")

# ======================================================
# LOAD FACT_NAV
# ======================================================

nav = pd.read_csv("data/processed/02_nav_history.csv")

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False,
)

print("fact_nav loaded successfully!")

# ======================================================
# LOAD FACT_TRANSACTIONS
# ======================================================

transactions = pd.read_csv(
    "data/processed/08_investor_transactions.csv"
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False,
)

print("fact_transactions loaded successfully!")

# ======================================================
# LOAD FACT_PERFORMANCE
# ======================================================

performance = pd.read_csv(
    "data/processed/07_scheme_performance.csv"
)

fact_performance = performance[
    [
        "amfi_code",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "benchmark_3yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "expense_ratio_pct",
        "morningstar_rating",
    ]
]

fact_performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False,
)

print("fact_performance loaded successfully!")

# ======================================================
# LOAD FACT_AUM
# ======================================================

fact_aum = performance[
    [
        "amfi_code",
        "aum_crore",
    ]
]

fact_aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False,
)

print("fact_aum loaded successfully!")

# ======================================================
# CREATE DIM_DATE
# ======================================================

nav["date"] = pd.to_datetime(nav["date"])

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

dates = pd.concat(
    [
        nav["date"],
        transactions["transaction_date"],
    ]
).drop_duplicates()

dim_date = pd.DataFrame()

dim_date["date"] = dates.dt.strftime("%Y-%m-%d")
dim_date["day"] = dates.dt.day
dim_date["month"] = dates.dt.month
dim_date["year"] = dates.dt.year

dim_date = dim_date.sort_values("date")

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False,
)

print("dim_date loaded successfully!")

# ======================================================
# VERIFY ROW COUNTS
# ======================================================

print("\n")
print("=" * 60)
print("VERIFYING TABLE ROW COUNTS")
print("=" * 60)

tables = [
    "dim_fund",
    "dim_date",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum",
]

for table in tables:
    rows = pd.read_sql(
        f"SELECT COUNT(*) AS total_rows FROM {table}",
        engine,
    )

    print(f"{table}")
    print(rows)
    print()

print("=" * 60)
print("ALL TABLES LOADED SUCCESSFULLY!")
print("=" * 60)