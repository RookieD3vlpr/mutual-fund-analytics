# Mutual Fund Analytics - Data Dictionary

## Database: `bluestock_mf.db` (SQLite)
This database uses a Star Schema design to model mutual fund performance and investor transactions.

### 1. `dim_fund` (Dimension Table)
Contains master details of all mutual funds.
* `amfi_code` (INTEGER): Primary Key. Unique identifier assigned by AMFI.
* `fund_house` (TEXT): Name of the Asset Management Company (e.g., SBI Mutual Fund).
* `scheme_name` (TEXT): Full name of the mutual fund scheme.
* `category` (TEXT): Asset class (Equity, Debt, Hybrid).
* `sub_category` (TEXT): Specific classification (Large Cap, Small Cap).
* `risk_grade` (TEXT): Risk level associated with the fund.

### 2. `fact_nav` (Fact Table)
Contains daily Net Asset Value (NAV) history.
* `amfi_code` (INTEGER): Foreign Key linking to `dim_fund`.
* `date` (DATE): Date of the NAV record.
* `nav` (REAL): Net Asset Value on the given date.

### 3. `fact_transactions` (Fact Table)
Records of individual investor purchases and redemptions.
* `investor_id` (INTEGER): Unique ID for the investor.
* `transaction_date` (DATE): Date the transaction occurred.
* `amfi_code` (INTEGER): Foreign Key linking to `dim_fund`.
* `transaction_type` (TEXT): Type of transaction (SIP, LUMPSUM, REDEMPTION).
* `amount_inr` (REAL): Transaction value in Indian Rupees.
* `state` / `city_tier` / `age_group` / `gender`: Investor demographics.
* `kyc_status` (TEXT): KYC verification status (VERIFIED, PENDING, REJECTED).

### 4. `fact_performance` (Fact Table)
Long-term return metrics and fund characteristics.
* `amfi_code` (INTEGER): Primary Key / Foreign Key linking to `dim_fund`.
* `1yr_return` / `3yr_return` / `5yr_return` (REAL): Annualized percentage returns.
* `expense_ratio` (REAL): Annual maintenance charge as a percentage.
* `fund_size_cr` (REAL): Total fund size in Crores.

### 5. `fact_aum` (Fact Table)
Total Assets Under Management per Fund House.
* `fund_house` (TEXT): Name of the AMC.
* `date` (DATE): Reporting date.
* `total_aum_cr` (REAL): Total AUM in Crores.