# 📊 End-to-End Mutual Fund Analytics Pipeline & Recommender Engine

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

---

# 📈 End-to-End Mutual Fund Analytics Pipeline & Recommender Engine

## 📝 Overview

This repository contains a comprehensive, production-grade **Data Engineering, Analytics, and Investment Recommendation Pipeline** built for the mutual fund industry.

The project ingests raw financial datasets, performs automated data cleaning and anomaly detection, transforms the data into a relational SQL Star Schema, computes institutional-grade performance and risk metrics, and visualizes insights through an interactive Power BI dashboard.

The capstone culminates in an intelligent **CLI-Based Mutual Fund Recommender Engine** that suggests optimized schemes based on investor risk appetite and quantitative performance metrics.

---

## ✨ Key Capabilities & Features

### 🔹 1. Robust Data Engineering (ETL)

- Automated data cleaning and validation
- Detection and correction of anomalous NAV values
- Rolling-median outlier filtering
- Feature engineering from mutual fund metadata
- Classification of:
  - Direct vs Regular Plans
  - Growth vs IDCW Options
- Transaction validation and business rule enforcement
- Detection of unusually large retail inflows (> ₹50 Lakhs)

---

### 🔹 2. Quantitative Performance Analytics

Computed advanced financial performance metrics across multiple mutual fund schemes benchmarked against the Nifty 50 Index.

#### Returns Metrics

- Daily Returns
- 1-Year CAGR
- 3-Year CAGR

#### Risk Metrics

- Annualized Volatility
- Maximum Drawdown
- Historical VaR (95%)
- Conditional VaR (CVaR)

#### Risk-Adjusted Metrics

- Sharpe Ratio
- Sortino Ratio
- Alpha (Outperformance)
- Beta (Market Sensitivity)

#### Proprietary Ranking Model

- Fund Scorecard (0–100)
- Risk-adjusted ranking methodology
- Multi-factor performance evaluation

---

### 🔹 3. Advanced Risk & Behavioral Modeling

#### Concentration Risk Analysis

- Herfindahl-Hirschman Index (HHI)
- Sector concentration monitoring
- Portfolio diversification assessment

#### Rolling Risk Analytics

- 90-Day Rolling Sharpe Ratio
- Dynamic volatility tracking
- Risk instability detection

#### Investor Cohort Analysis

- Investor vintage tracking
- SIP continuity analysis
- Churn prediction indicators
- Detection of inactive investors (>35 days)

---

### 🔹 4. Interactive Power BI Dashboard

A fully interactive multi-page executive dashboard featuring:

### Industry Overview

- Total AUM KPIs
- Industry-wide SIP volumes
- Historical growth trends
- Fund category distributions

### Fund Performance

- Risk vs Return Scatter Plot
- Benchmark comparisons
- Interactive Fund Scorecards
- Performance rankings

### Investor Demographics

- Geographic investment heatmaps
- Age-group participation analysis
- SIP vs Lumpsum behavior
- Investor segmentation

### Market Trends

- SIP Inflows vs Benchmark Index
- Category-wise inflow heatmaps
- Sector allocation trends
- Market sentiment indicators

---

## 📂 Project Structure

```text
mutual_fund_analytics/
│
├── data/
│   ├── raw/                         # Raw, uncleaned CSV files
│   └── processed/                   # Cleaned fact and dimension tables
│
├── db/
│   └── bluestock_mf.db              # SQLite Database (Star Schema)
│
├── notebooks/
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── Advanced_Analytics.ipynb     # VaR, HHI & Cohort Analysis
│
├── scripts/
│   ├── data_cleaning.py             # ETL & Data Validation Pipeline
│   └── recommender.py               # CLI Recommendation Engine
│
├── reports/
│   ├── fund_scorecard.csv
│   ├── var_cvar_report.csv
│   └── *.png                        # Generated Charts & Visuals
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   └── Dashboard.pdf
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Technology Stack

### Programming

- Python 3

### Data Engineering

- Pandas
- NumPy
- SciPy

### Database

- SQLite
- SQLAlchemy
- SQL

### Visualization

- Matplotlib
- Seaborn
- Plotly
- Power BI

### Development Environment

- VS Code
- Jupyter Notebook
- Git & GitHub

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/mutual-fund-analytics.git
cd mutual-fund-analytics
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Data Pipeline

Execute the ETL and anomaly detection workflow:

```bash
python scripts/data_cleaning.py
```

This will:

- Clean raw datasets
- Detect NAV anomalies
- Engineer features
- Generate processed tables
- Populate the SQLite database

---

## 🤖 Launch the Recommender Engine

Run the command-line recommendation engine:

```bash
python scripts/recommender.py
```

### User Inputs

Select a risk profile:

- Low Risk
- Moderate Risk
- High Risk

### Engine Outputs

Returns the:

- Top 3 Recommended Schemes
- Sharpe Ratios
- CAGR Scores
- Fund Scorecard Rankings

---

## 📈 Dashboard Preview

### Risk vs Return Analysis

Visualizes the efficient frontier of tracked mutual fund schemes using:

- Expected Return
- Annualized Volatility
- Fund AUM

### Category Flow Heatmaps

Tracks capital movement across:

- Equity Funds
- Debt Funds
- Hybrid Funds

over a multi-year period.

### Executive KPI Monitoring

Displays:

- Total Industry AUM
- SIP Volumes
- Investor Growth Trends
- Category Performance Metrics

---

## 📊 Analytical Outputs

### Generated Reports

- Fund Scorecard
- Alpha/Beta Analysis
- VaR & CVaR Reports
- Cohort Analysis Reports
- Benchmark Comparison Reports

### Visualizations

- Risk vs Return Scatter Plots
- Rolling Sharpe Ratio Charts
- SIP Trend Analysis
- Investor Demographic Visuals
- Geographic Distribution Maps
- Sector Allocation Charts
- Category Heatmaps

---

## 🎯 Project Outcomes

This project demonstrates:

- End-to-End Data Engineering
- Financial Data Analytics
- Quantitative Risk Modeling
- Database Design
- Dashboard Development
- Portfolio Recommendation Systems
- Business Intelligence Reporting

---

## 📈 Project Status

| Module | Status |
|----------|----------|
| Data Engineering Pipeline | ✅ Complete |
| Data Cleaning & Validation | ✅ Complete |
| SQL Database Design | ✅ Complete |
| Exploratory Data Analysis | ✅ Complete |
| Performance Analytics | ✅ Complete |
| Risk Modeling | ✅ Complete |
| Fund Recommendation Engine | ✅ Complete |
| Power BI Dashboard | 🚧 In Progress |
| Final Reporting | 🚧 In Progress |

### Overall Progress

**90% Complete 🚀**

---

## 👨‍💻 Capstone Information

**Program:** BlueStock FinTech Engineering Track

**Project:** End-to-End Mutual Fund Analytics Pipeline & Recommender Engine

**Domain:** Financial Analytics & Investment Intelligence

**Year:** 2026

---

## 🚀 GitHub Sync

```bash
git add README.md
git commit -m "Added professional project documentation"
git push origin main
```

---

## 📜 License

This project was developed for educational, research, and internship purposes as part of the BlueStock FinTech Engineering Track.