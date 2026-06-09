import pandas as pd
import numpy as np
import logging
import warnings
from pathlib import Path

# Suppress pandas warnings for cleaner console output
warnings.filterwarnings('ignore')

# ---------------------------------------------------------
# Logging Configuration
# ---------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('MF_DataPipeline')

# ---------------------------------------------------------
# Pipeline Class Definition
# ---------------------------------------------------------
class MutualFundDataCleaner:
    """
    An enterprise-grade ETL cleaner for Mutual Fund data streams.
    Handles anomaly detection, feature engineering, and memory optimization.
    """
    
    def __init__(self, raw_dir: str = '../data/raw', processed_dir: str = '../data/processed'):
        self.raw_dir = Path(raw_dir)
        self.processed_dir = Path(processed_dir)
        self._setup_directories()

    def _setup_directories(self) -> None:
        """Ensures the processed output directory exists."""
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Pipeline initialized. Output directory: {self.processed_dir}")

    def clean_nav_data(self) -> None:
        """Advanced NAV cleaning: Outlier detection and business-day alignment."""
        logger.info("Starting NAV Data processing...")
        raw_path = self.raw_dir / 'raw_nav_data.csv'
        processed_path = self.processed_dir / 'cleaned_fact_nav.csv'

        if not raw_path.exists():
            logger.warning(f"File not found: {raw_path}. Skipping NAV pipeline.")
            return

        try:
            df_nav = pd.read_csv(raw_path)
            
            # 1. Standardize Dates & Types
            df_nav['date'] = pd.to_datetime(df_nav['date'], format='mixed', dayfirst=True)
            df_nav['nav'] = pd.to_numeric(df_nav['nav'], errors='coerce')
            df_nav = df_nav.dropna(subset=['nav', 'amfi_code'])
            
            # Optimize Memory by ensuring AMFI codes are strings
            df_nav['amfi_code'] = df_nav['amfi_code'].astype(str).str.strip()

            # 2. Anomaly Detection (Rolling Median)
            # Detects flash crashes and fat-finger errors
            df_nav = df_nav.sort_values(by=['amfi_code', 'date'])
            df_nav['rolling_median'] = df_nav.groupby('amfi_code')['nav'].rolling(
                window=5, center=True, min_periods=1
            ).median().reset_index(0, drop=True)
            
            df_nav['deviation'] = abs((df_nav['nav'] - df_nav['rolling_median']) / df_nav['rolling_median'])
            
            initial_rows = len(df_nav)
            df_nav = df_nav[df_nav['deviation'] <= 0.15] # Keep rows within 15% deviation
            outliers_removed = initial_rows - len(df_nav)

            # 3. Cleanup & Export
            df_nav = df_nav.drop(columns=['rolling_median', 'deviation'])
            df_nav.to_csv(processed_path, index=False)
            
            logger.info(f"NAV Data cleaned | Outliers removed: {outliers_removed} | Rows finalized: {len(df_nav)}")

        except Exception as e:
            logger.error(f"Critical error during NAV cleaning: {str(e)}")

    def clean_fund_metadata(self) -> None:
        """Advanced Metadata cleaning: NLP Feature Extraction and Categorization."""
        logger.info("Starting Fund Metadata processing...")
        raw_path = self.raw_dir / 'raw_fund_metadata.csv'
        processed_path = self.processed_dir / 'cleaned_dim_fund.csv'

        if not raw_path.exists():
            logger.warning(f"File not found: {raw_path}. Skipping Metadata pipeline.")
            return

        try:
            df_funds = pd.read_csv(raw_path)
            
            # 1. Text Normalization
            df_funds['scheme_name'] = df_funds['scheme_name'].str.strip().str.title()
            
            # 2. Feature Engineering
            df_funds['plan_type'] = np.where(
                df_funds['scheme_name'].str.contains('Direct', case=False), 'Direct', 'Regular'
            )
            df_funds['option_type'] = np.where(
                df_funds['scheme_name'].str.contains('Growth| Gr', case=False, regex=True), 'Growth', 'IDCW/Dividend'
            )
            
            # 3. Categorical Standardization
            cat_map = {
                'Eq': 'Equity', 'Equity Scheme': 'Equity',
                'Debt Scheme': 'Debt', 'Liquid': 'Debt', 
                'Hybrid Scheme': 'Hybrid'
            }
            df_funds['category'] = df_funds['category'].replace(cat_map)
            
            # Memory Optimization: Convert low-cardinality strings to Categorical data types
            df_funds['category'] = df_funds['category'].astype('category')
            df_funds['plan_type'] = df_funds['plan_type'].astype('category')
            
            df_funds.to_csv(processed_path, index=False)
            logger.info(f"Fund Metadata cleaned | Engineered features added | Rows finalized: {len(df_funds)}")

        except Exception as e:
            logger.error(f"Critical error during Metadata cleaning: {str(e)}")

    def clean_transactions(self) -> None:
        """Advanced Transaction cleaning: Logic enforcement and Threshold bounds."""
        logger.info("Starting Transaction Data processing...")
        raw_path = self.raw_dir / 'raw_transactions.csv'
        processed_path = self.processed_dir / 'cleaned_fact_transactions.csv'

        if not raw_path.exists():
            logger.warning(f"File not found: {raw_path}. Skipping Transaction pipeline.")
            return

        try:
            df_trans = pd.read_csv(raw_path)
            
            # 1. Parsing and Formatting
            df_trans['transaction_date'] = pd.to_datetime(df_trans['transaction_date'], format='mixed')
            
            if df_trans['amount_inr'].dtype == 'O':
                df_trans['amount_inr'] = df_trans['amount_inr'].str.replace(r'[₹,]', '', regex=True)
            df_trans['amount_inr'] = pd.to_numeric(df_trans['amount_inr'], errors='coerce')
            df_trans = df_trans.dropna(subset=['amount_inr'])
            
            # 2. Business Logic Enforcement
            # Ensure SIPs are never negative
            df_trans['amount_inr'] = np.where(
                df_trans['transaction_type'] == 'SIP', 
                df_trans['amount_inr'].abs(), 
                df_trans['amount_inr']
            )
            
            # 3. Contextual Anomaly Flagging
            # Flag massive retail inflows (> 50 Lakhs) and micro-entries (< 100 Rs)
            df_trans['is_anomaly'] = np.where(
                ((df_trans['transaction_type'] == 'SIP') & (df_trans['amount_inr'] > 5000000)) | 
                (df_trans['amount_inr'] < 100), 
                True, False
            )
            
            anomalies_flagged = df_trans['is_anomaly'].sum()
            df_trans.to_csv(processed_path, index=False)
            logger.info(f"Transaction Data cleaned | Anomalies flagged: {anomalies_flagged} | Rows finalized: {len(df_trans)}")

        except Exception as e:
            logger.error(f"Critical error during Transaction cleaning: {str(e)}")

    def run_all(self) -> None:
        """Executes the full pipeline sequentially."""
        logger.info("🚀 Initiating Full Data Cleaning Pipeline...")
        self.clean_nav_data()
        self.clean_fund_metadata()
        self.clean_transactions()
        logger.info("🎉 Pipeline execution completed successfully!")

# ---------------------------------------------------------
# Execution Entry Point
# ---------------------------------------------------------
if __name__ == "__main__":
    pipeline = MutualFundDataCleaner()
    pipeline.run_all()