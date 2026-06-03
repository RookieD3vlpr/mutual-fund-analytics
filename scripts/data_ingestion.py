import pandas as pd
import glob
import os

print("--- Task 3: Load & Inspect CSVs ---")
csv_files = glob.glob('data/raw/*.csv') 
datasets = {}

for file in csv_files:
    filename = os.path.basename(file)
    print(f"\n[{filename}]")
    try:
        df = pd.read_csv(file)
        datasets[filename] = df
        
        print(f"Shape: {df.shape}")
        print(f"Data Types:\n{df.dtypes.to_string()}")
        print(f"Head:\n{df.head(2)}")
        
        # Anomaly Check
        if df.isnull().sum().sum() > 0:
            print(f"⚠️ ANOMALY: Missing values detected in {filename}.")
    except Exception as e:
        print(f"Error loading {filename}: {e}")

# Task 6: Explore Fund Master
if '01_fund_master.csv' in datasets:
    print("\n--- Task 6: Explore Fund Master ---")
    master = datasets['01_fund_master.csv']
    if 'fund_house' in master.columns:
        print(f"Unique Fund Houses: {master['fund_house'].nunique()}")
    if 'category' in master.columns:
        print(f"Unique Categories: {master['category'].unique()}")
    if 'sub_category' in master.columns:
        print(f"Unique Sub-categories: {master['sub_category'].unique()}")
    if 'risk_grade' in master.columns:
        print(f"Unique Risk Grades: {master['risk_grade'].unique()}")

# Task 7: Validate AMFI Codes
if '01_fund_master.csv' in datasets and '02_nav_history.csv' in datasets:
    print("\n--- Task 7: Validate AMFI Codes ---")
    
    # Both datasets use 'amfi_code' instead of 'scheme_code'
    master_codes = set(datasets['01_fund_master.csv']['amfi_code'].dropna().unique())
    history_codes = set(datasets['02_nav_history.csv']['amfi_code'].dropna().unique())
    
    missing_codes = master_codes - history_codes
    
    print(f"Codes in Fund Master: {len(master_codes)}")
    print(f"Codes in NAV History: {len(history_codes)}")
    
    if len(missing_codes) == 0:
        print("✅ PASS: All master codes exist in NAV history.")
    else:
        print(f"⚠️ FAIL: {len(missing_codes)} master codes missing in NAV history.")