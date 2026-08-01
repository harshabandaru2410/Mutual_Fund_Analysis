# Mutual Fund Analysis - Data Dictionary

## Overview

This document describes the tables, columns, data types, and business meaning of the Mutual Fund Analysis SQLite database.

---

# Table: dim_fund

Description:
Stores master information about every mutual fund.

| Column | Data Type | Description | Source |
|---------|-----------|-------------|--------|
| amfi_code | INTEGER | Unique AMFI code of the mutual fund | 01_fund_master.csv |
| scheme_name | TEXT | Name of the mutual fund scheme | 01_fund_master.csv |
| fund_house | TEXT | Asset Management Company (AMC) | 01_fund_master.csv |
| category | TEXT | Fund category | 01_fund_master.csv |
| sub_category | TEXT | Fund sub-category | 01_fund_master.csv |
| plan | TEXT | Regular or Direct Plan | 01_fund_master.csv |
| fund_manager | TEXT | Fund manager name | 01_fund_master.csv |
| risk_category | TEXT | Risk level | 01_fund_master.csv |

---

# Table: dim_date

Description:
Stores calendar information.

| Column | Data Type | Description |
|---------|-----------|-------------|
| date | TEXT | Calendar date |
| day | INTEGER | Day of month |
| month | INTEGER | Month |
| year | INTEGER | Year |

---

# Table: fact_nav

Description:
Stores daily NAV values.

| Column | Data Type | Description | Source |
|---------|-----------|-------------|--------|
| amfi_code | INTEGER | Mutual fund identifier | 02_nav_history.csv |
| date | TEXT | NAV date | 02_nav_history.csv |
| nav | REAL | Net Asset Value | 02_nav_history.csv |

---

# Table: fact_transactions

Description:
Stores investor transactions.

| Column | Data Type | Description | Source |
|---------|-----------|-------------|--------|
| investor_id | TEXT | Unique investor ID | 08_investor_transactions.csv |
| transaction_date | TEXT | Transaction date | 08_investor_transactions.csv |
| amfi_code | INTEGER | Fund identifier | 08_investor_transactions.csv |
| transaction_type | TEXT | SIP / Lumpsum / Redemption | 08_investor_transactions.csv |
| amount_inr | REAL | Investment amount | 08_investor_transactions.csv |
| state | TEXT | Investor state | 08_investor_transactions.csv |
| city | TEXT | Investor city | 08_investor_transactions.csv |
| city_tier | TEXT | Tier 1 / 2 / 3 | 08_investor_transactions.csv |
| age_group | TEXT | Investor age group | 08_investor_transactions.csv |
| gender | TEXT | Investor gender | 08_investor_transactions.csv |
| annual_income_lakh | REAL | Annual income (Lakhs) | 08_investor_transactions.csv |
| payment_mode | TEXT | Payment method | 08_investor_transactions.csv |
| kyc_status | TEXT | KYC verification status | 08_investor_transactions.csv |

---

# Table: fact_performance

Description:
Stores mutual fund performance metrics.

| Column | Data Type | Description | Source |
|---------|-----------|-------------|--------|
| amfi_code | INTEGER | Fund identifier | 07_scheme_performance.csv |
| return_1yr_pct | REAL | 1-Year Return (%) | 07_scheme_performance.csv |
| return_3yr_pct | REAL | 3-Year Return (%) | 07_scheme_performance.csv |
| return_5yr_pct | REAL | 5-Year Return (%) | 07_scheme_performance.csv |
| benchmark_3yr_pct | REAL | Benchmark Return (%) | 07_scheme_performance.csv |
| alpha | REAL | Alpha value | 07_scheme_performance.csv |
| beta | REAL | Beta value | 07_scheme_performance.csv |
| sharpe_ratio | REAL | Sharpe Ratio | 07_scheme_performance.csv |
| sortino_ratio | REAL | Sortino Ratio | 07_scheme_performance.csv |
| std_dev_ann_pct | REAL | Annual Standard Deviation | 07_scheme_performance.csv |
| max_drawdown_pct | REAL | Maximum Drawdown (%) | 07_scheme_performance.csv |
| expense_ratio_pct | REAL | Expense Ratio (%) | 07_scheme_performance.csv |
| morningstar_rating | INTEGER | Morningstar Rating | 07_scheme_performance.csv |

---

# Table: fact_aum

Description:
Stores Assets Under Management.

| Column | Data Type | Description | Source |
|---------|-----------|-------------|--------|
| amfi_code | INTEGER | Fund identifier | 07_scheme_performance.csv |
| aum_crore | INTEGER | Assets Under Management (₹ Crore) | 07_scheme_performance.csv |