import requests
import pandas as pd
import os

# Ensure raw data folder exists
os.makedirs('data/raw', exist_ok=True)

def fetch_and_save_nav(scheme_code, fund_name):
    """Fetches NAV data from mfapi.in and saves as CSV."""
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and len(data['data']) > 0:
            df = pd.DataFrame(data['data'])
            df['scheme_code'] = scheme_code 
            
            # Save file
            clean_name = fund_name.replace(' ', '_').lower()
            filename = f"data/raw/{scheme_code}_{clean_name}.csv"
            df.to_csv(filename, index=False)
            print(f"Success: {fund_name} saved ({len(df)} records).")
        else:
            print(f"Warning: No data for {fund_name}.")
    else:
        print(f"Error: Request failed for {scheme_code}.")

# Task 4: Target Scheme
print("--- Fetching HDFC Top 100 Direct ---")
fetch_and_save_nav(125497, "HDFC Top 100 Direct")

# Task 5: Key Benchmark Schemes
print("\n--- Fetching Key Schemes ---")
benchmarks = {
    119551: "SBI Bluechip",
    120503: "ICICI Bluechip",
    118632: "Nippon Large Cap",
    119092: "Axis Bluechip",
    120841: "Kotak Bluechip"
}

for code, name in benchmarks.items():
    fetch_and_save_nav(code, name)