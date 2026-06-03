-- 1. Top 5 funds by AUM (Assets Under Management)
SELECT fund_house, MAX(total_aum_cr) as max_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY max_aum DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT strftime('%Y-%m', date) AS month, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. SIP YoY (Year-over-Year) growth (Total SIP amount per year)
SELECT strftime('%Y', transaction_date) AS year, SUM(amount_inr) AS total_sip_volume
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- 4. Transactions by State
SELECT state, COUNT(investor_id) AS total_transactions, SUM(amount_inr) AS total_volume_inr
FROM fact_transactions
GROUP BY state
ORDER BY total_volume_inr DESC;

-- 5. Funds with expense_ratio < 1%
SELECT d.scheme_name, p.expense_ratio
FROM dim_fund d
JOIN fact_performance p ON d.amfi_code = p.amfi_code
WHERE p.expense_ratio < 1.0
ORDER BY p.expense_ratio ASC;

-- 6. (Custom) Top 5 Funds by 5-Year Return
SELECT d.scheme_name, d.category, p."5yr_return"
FROM dim_fund d
JOIN fact_performance p ON d.amfi_code = p.amfi_code
ORDER BY p."5yr_return" DESC
LIMIT 5;

-- 7. (Custom) SIP vs Lumpsum Investment Comparison
SELECT transaction_type, SUM(amount_inr) AS total_invested
FROM fact_transactions
WHERE transaction_type IN ('SIP', 'LUMPSUM')
GROUP BY transaction_type;

-- 8. (Custom) Average Transaction Amount by Age Group
SELECT age_group, AVG(amount_inr) AS avg_txn_amount
FROM fact_transactions
GROUP BY age_group
ORDER BY avg_txn_amount DESC;

-- 9. (Custom) Investor Count by KYC Status
SELECT kyc_status, COUNT(DISTINCT investor_id) AS total_investors
FROM fact_transactions
GROUP BY kyc_status;

-- 10. (Custom) Fund Category Distribution
SELECT category, COUNT(amfi_code) AS number_of_funds
FROM dim_fund
GROUP BY category
ORDER BY number_of_funds DESC;