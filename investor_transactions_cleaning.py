import pandas as pd 
import os 
RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"
transactions = pd.read_csv(os.path.join(RAW_FOLDER,"08_investor_transactions.csv"))
#BASIC DATA
print("="*70)
print("investor transaction data set")
print("="*70)
print("\ncolumns:")
print(transactions.columns.tolist())
print("\nfirst 5 rows:")
print(transactions.head())
print("\nshape:")
print(transactions.shape)
print("\ndata types")
print(transactions.dtypes)
print("\n missing values ")
print(transactions.isnull().sum())
print("\n duplicate rows ")
print(transactions.duplicated().sum())

transactions["transaction_date"]=pd.to_datetime(transactions["transaction_date"])
#standardization
print("\nUnique Transaction Types")
print(transactions["transaction_type"].unique())

#PRINTING INVALID AMOUNT
invalid_amount=transactions[transactions["amount_inr"]<=0]
print("\n invalid amount records")
print(invalid_amount)

#removing inVALID rows
transactions=transactions[transactions["amount_inr"]>0]

#PRINTING MINIMUM AMOUNT
print("\n minimum transaction amount")
print(transactions["amount_inr"].min())

#VALIDATE KYC STATUS
print("\nunique KYC status values")
print(transactions["kyc_status"].unique())
valid_kyc = [
    "Verified",
    "Pending"
]
#Find invalid values
invalid_kyc = transactions[
    ~transactions["kyc_status"].isin(valid_kyc)
]

print("\nInvalid KYC Records")
print(invalid_kyc)
print("\nNumber of Invalid KYC Records")
print(len(invalid_kyc))

#SAVING 
transactions.to_csv(os.path.join(PROCESSED_FOLDER,"08_investor_transactions.csv"),index=False)
print("\nCleaned investor_transactions.csv saved successfully!")