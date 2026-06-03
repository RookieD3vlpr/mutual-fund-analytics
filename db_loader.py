import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import os

print("--- Starting Phase 2: Database Build & Load ---")

db_name = 'bluestock_mf.db'

# 0. Delete old database to prevent duplicate data on re-runs
if os.path.exists(db_name):
    os.remove(db_name)
    print(f"Cleared old {db_name} to start fresh.")

# 1. Create SQLite Engine & Database file
engine = create_engine(f'sqlite:///{db_name}')

# 2. Execute Schema to enforce Primary/Foreign keys
print("Applying Star Schema constraints...")
with sqlite3.connect(db_name) as conn:
    with open('sql/schema.sql', 'r') as f:
        conn.executescript(f.read())

# 3. Map database tables to your processed CSVs
tables_to_load = {
    'dim_fund': 'data/processed/clean_fund_master.csv',
    'fact_nav': 'data/processed/clean_nav_history.csv',
    'fact_transactions': 'data/processed/clean_investor_transactions.csv',
    'fact_performance': 'data/processed/clean_scheme_performance.csv',
    'fact_aum': 'data/processed/clean_aum_by_fund_house.csv'
}

# 4. Load Data using Pandas
for table_name, csv_path in tables_to_load.items():
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        
        # Fetch the columns we explicitly defined in our SQL schema
        schema_cols = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 0", engine).columns
        
        # Filter the dataframe to ONLY include columns that exist in the database table
        df_filtered = df[[col for col in df.columns if col in schema_cols]]
        
        # Load the filtered data
        df_filtered.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"✅ Loaded {len(df_filtered)} rows into {table_name}")
    else:
        print(f"⚠️ Warning: Could not find {csv_path}")

print("\n--- Phase 2 Complete! bluestock_mf.db is ready. ---")