-- Query 1(Top fund houses by AUM)
SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM fact_performance
GROUP BY fund_house
ORDER BY total_aum DESC;

-- Query 2(Top funds by Sharpe Ratio)
SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- Query 3(Average Expense Ratio by Fund House)
SELECT
    fund_house,
    AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance
GROUP BY fund_house;

--Query 4 — Top 5 Funds by AUM
SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

--Query 5 — Funds with Expense Ratio < 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

--Query 6 — Average Sharpe Ratio by Fund House
SELECT
    fund_house,
    AVG(sharpe_ratio) AS avg_sharpe
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_sharpe DESC;

-- Query 7 — Top 5 Funds by 5-Year Return
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Query 8 — Total Transactions by Type
SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- Query 9 — Total Transaction Amount by Type
SELECT
    transaction_type,
    SUM(amount) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- Query 10 — KYC Status Distribution
SELECT
    kyc_status,
    COUNT(*) AS investors
FROM fact_transactions
GROUP BY kyc_status;
