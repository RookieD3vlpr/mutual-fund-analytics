import pandas as pd
import numpy as np
import glob
import os

print("--- Starting Data Cleaning Pipeline ---")

# Ensure processed folder exists
os.makedirs('data/processed', exist_ok=True)

# Helper function to get correct filename from raw folder
def get_file(keyword):
    files = glob.glob(f'data/raw/*{keyword}*.csv')
    return files[0] if files else None

# ---------------------------------------------------------
# Task 1: Clean NAV History
# ---------------------------------------------------------
nav_file = get_file('nav_history')
if nav_file:
    print("\nCleaning NAV History...")
    df_nav = pd.read_csv(nav_file)
    
    # Parse dates
    df_nav['date'] = pd.to_datetime(df_nav['date'], format='mixed')
    
    # Sort by code and date
    df_nav = df_nav.sort_values(by=['amfi_code', 'date'])
    
    # Validate NAV > 0
    df_nav = df_nav[df_nav['nav'] > 0]
    
    # Remove duplicates
    df_nav = df_nav.drop_duplicates(subset=['amfi_code', 'date'])
    
    # Forward-fill missing dates for holidays/weekends
    # Group by amfi_code, resample to daily ('D'), and forward fill (ffill)
    # Forward-fill missing dates for holidays/weekends
    df_nav = df_nav.set_index('date').groupby('amfi_code')['nav'].resample('D').ffill().reset_index()
    
    df_nav.to_csv('data/processed/clean_nav_history.csv', index=False)
    print(f"✅ Saved clean_nav_history.csv | Records: {len(df_nav)}")

# ---------------------------------------------------------
# Task 2: Clean Investor Transactions
# ---------------------------------------------------------
txn_file = get_file('investor_transactions')
if txn_file:
    print("\nCleaning Investor Transactions...")
    df_txn = pd.read_csv(txn_file)
    
    # Standardise transaction_type
    df_txn['transaction_type'] = df_txn['transaction_type'].str.upper().str.strip()
    valid_types = ['SIP', 'LUMPSUM', 'REDEMPTION']
    df_txn = df_txn[df_txn['transaction_type'].isin(valid_types)]
    
    # Validate amount > 0
    df_txn = df_txn[df_txn['amount_inr'] > 0]
    
    # Fix date formats
    df_txn['transaction_date'] = pd.to_datetime(df_txn['transaction_date'], format='mixed')
    
    # Check KYC status
    valid_kyc = ['VERIFIED', 'PENDING', 'REJECTED']
    df_txn['kyc_status'] = df_txn['kyc_status'].str.upper().str.strip()
    df_txn['kyc_status'] = np.where(df_txn['kyc_status'].isin(valid_kyc), df_txn['kyc_status'], 'UNKNOWN')
    
    df_txn.to_csv('data/processed/clean_investor_transactions.csv', index=False)
    print(f"✅ Saved clean_investor_transactions.csv | Records: {len(df_txn)}")

# ---------------------------------------------------------
# Task 3: Clean Scheme Performance
# ---------------------------------------------------------
perf_file = get_file('scheme_performance')
if perf_file:
    print("\nCleaning Scheme Performance...")
    df_perf = pd.read_csv(perf_file)
    
    # Validate returns are numeric (coerce errors to NaN, then drop or flag)
    return_cols = ['1yr_return', '3yr_return', '5yr_return']
    for col in return_cols:
        if col in df_perf.columns:
            df_perf[col] = pd.to_numeric(df_perf[col], errors='coerce')
    
    # Expense ratio check (0.1% - 2.5%)
    if 'expense_ratio' in df_perf.columns:
        df_perf = df_perf[(df_perf['expense_ratio'] >= 0.1) & (df_perf['expense_ratio'] <= 2.5)]
        
    df_perf.to_csv('data/processed/clean_scheme_performance.csv', index=False)
    print(f"✅ Saved clean_scheme_performance.csv | Records: {len(df_perf)}")

# ---------------------------------------------------------
# Task 4: Move remaining datasets as-is to processed
# ---------------------------------------------------------
print("\nMoving remaining datasets to processed folder...")
all_raw_files = glob.glob('data/raw/*.csv')
cleaned_keywords = ['nav_history', 'investor_transactions', 'scheme_performance']

for file in all_raw_files:
    filename = os.path.basename(file)
    # If the file wasn't one of the three we just cleaned, copy it over
    if not any(keyword in filename for keyword in cleaned_keywords):
        df = pd.read_csv(file)
        clean_name = f"clean_{filename.split('_', 1)[-1]}" if filename[0].isdigit() else f"clean_{filename}"
        df.to_csv(f'data/processed/{clean_name}', index=False)

print("\n--- Phase 1 Complete! ---")