-- Dimension: Fund Master
CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    risk_grade TEXT
);

-- Fact: NAV History
CREATE TABLE IF NOT EXISTS fact_nav (
    amfi_code INTEGER,
    date DATE,
    nav REAL,
    PRIMARY KEY (amfi_code, date),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- Fact: Investor Transactions
CREATE TABLE IF NOT EXISTS fact_transactions (
    investor_id INTEGER,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- Fact: Scheme Performance
CREATE TABLE IF NOT EXISTS fact_performance (
    amfi_code INTEGER PRIMARY KEY,
    "1yr_return" REAL,
    "3yr_return" REAL,
    "5yr_return" REAL,
    expense_ratio REAL,
    fund_size_cr REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- Fact: AUM by Fund House
CREATE TABLE IF NOT EXISTS fact_aum (
    fund_house TEXT,
    date DATE,
    total_aum_cr REAL,
    PRIMARY KEY (fund_house, date)
);