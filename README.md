# 📈 Mutual Fund Analytics Capstone

## 📝 Project Overview

This repository contains the code, data pipelines, and analytical models for the **Mutual Fund Analytics Capstone Project**, developed as part of the **BlueStock Fintech Data Analyst Internship**.

The objective of this project is to build an end-to-end data analytics pipeline that extracts live mutual fund data, processes historical financial datasets, and generates actionable investment insights using Python, SQL, and interactive dashboards.

---

## 🗂️ Project Structure

```text
mutual_fund_analytics/
│
├── data/
│   ├── raw/                 # Original downloaded CSV files and API data
│   ├── processed/           # Cleaned and transformed datasets
│   └── db/                  # bluestock_mf.db (SQLite database)
│
├── notebooks/               # Jupyter Notebooks for EDA and advanced analytics
│   ├── 03_eda_analysis.ipynb
│   └── 04_performance_analytics.ipynb
│
├── scripts/                 # Python ETL pipeline scripts (fetching, cleaning, loading)
│
├── sql/                     # PostgreSQL/SQLite schema and analytical queries
│
├── dashboard/               # Interactive dashboard assets (Power BI / Web App)
│
├── reports/                 # Static charts, CSV outputs, and presentations
│   ├── alpha_beta.csv
│   ├── aum_growth_sbi.png
│   ├── benchmark_comparison.png
│   ├── category_inflow_heatmap.png
│   ├── fund_scorecard.csv
│   ├── geographic_distribution.png
│   ├── investor_demographics.png
│   ├── nav_return_correlation.png
│   ├── nav_trend_analysis.png
│   ├── sector_allocation_donut.png
│   └── sip_inflow_trend.png
│
├── .gitignore               # Excluded files (e.g., *.db files, virtual environments)
├── data_dictionary.md       # Business definitions and schema documentation
├── requirements.txt         # Python library dependencies
└── README.md                # Project documentation
```

---

## 🛠️ Tech Stack & Tools

### Programming
- Python 3

### Data Manipulation & Analysis
- NumPy
- Pandas
- SciPy

### Database Management
- SQLite
- SQLAlchemy
- SQL

### Data Visualization
- Matplotlib
- Seaborn
- Plotly

### Development Environment
- VS Code
- Jupyter Notebook
- Git/GitHub

---

## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/mutual-fund-analytics.git
cd mutual-fund-analytics
```

### 2. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the ETL Pipeline

#### Fetch Live Mutual Fund Data

```bash
python scripts/live_nav_fetch.py
```

#### Clean Historical Datasets

```bash
python scripts/data_cleaning.py
```

#### Load Data into SQLite

```bash
python scripts/db_loader.py
```

---

## 📊 Analytics Notebooks

### Exploratory Data Analysis

Open:

```text
notebooks/03_eda_analysis.ipynb
```

This notebook contains:
- AUM Growth Analysis
- SIP Inflow Trends
- Investor Demographics Analysis
- Geographic Distribution Analysis
- Sector Allocation Analysis
- NAV Trend Analysis
- Correlation Analysis
- Category-wise Fund Performance Insights

### Performance Analytics

Open:

```text
notebooks/04_performance_analytics.ipynb
```

This notebook contains:
- Daily Return Calculations
- CAGR Analysis
- Sharpe Ratio
- Sortino Ratio
- Alpha & Beta Estimation
- Maximum Drawdown Analysis
- Benchmark Comparison
- Proprietary Fund Scorecard Model

---

## 📈 Key Insights Generated

### Exploratory Data Analysis

- AUM Growth Trends
- SIP Inflow Analysis
- Category Inflow Heatmaps
- Investor Demographics
- Geographic Distribution
- NAV Trend Analysis
- Risk-Return Correlation Analysis
- Sector Allocation Breakdown

### Performance Analytics

- CAGR Rankings
- Sharpe Ratio Rankings
- Sortino Ratio Rankings
- Alpha/Beta Comparisons
- Maximum Drawdown Evaluation
- Benchmark Outperformance Analysis
- Fund Scorecard Rankings

---

## 📊 Current Progress

### ✅ Day 1: Project Setup & ETL

- Configured development environment
- Built API extraction scripts
- Validated local CSV integrity
- Created project structure

### ✅ Day 2: Data Cleaning & SQL Database

- Cleaned datasets using Pandas
- Designed Star Schema architecture
- Loaded processed data into SQLite
- Developed analytical SQL queries

### ✅ Day 3: Exploratory Data Analysis (EDA)

- Generated 10 analytical visualizations
- Conducted trend analysis
- Performed correlation analysis
- Identified business insights
- Created presentation-ready charts

### ✅ Day 4: Fund Performance Analytics

- Computed Daily Returns
- Calculated CAGR
- Calculated Sharpe Ratio
- Calculated Sortino Ratio
- Calculated Alpha & Beta
- Measured Maximum Drawdowns
- Built Proprietary Fund Scorecard (0–100)
- Generated Benchmark Comparison Charts

### ⬜ Day 5: Dashboards & Final Reporting

- Interactive Dashboard Development
- Business Presentation Preparation
- Final Report Compilation
- Project Demonstration Assets

---

## 📈 Project Status

| Module | Status |
|----------|----------|
| ETL Pipeline | ✅ Complete |
| Data Cleaning | ✅ Complete |
| Database Design | ✅ Complete |
| SQL Analytics | ✅ Complete |
| Exploratory Data Analysis | ✅ Complete |
| Performance Analytics | ✅ Complete |
| Dashboard Development | ⬜ In Progress |
| Final Reporting | ⬜ In Progress |

### Overall Completion

**85% Complete** 🚀

---

## 📂 Outputs Generated

### Charts

- AUM Growth Analysis
- SIP Inflow Trend Analysis
- NAV Trend Analysis
- NAV Return Correlation Matrix
- Investor Demographics Visualization
- Geographic Distribution Map
- Category Inflow Heatmap
- Sector Allocation Donut Chart
- Benchmark Comparison Charts

### Data Products

- Alpha/Beta Dataset
- Fund Scorecard Dataset
- Processed Mutual Fund Database
- SQL Analytics Reports

---

## 🎯 Project Objectives

- Automate Mutual Fund Data Collection
- Build a Scalable ETL Pipeline
- Design a Relational Financial Database
- Perform Quantitative Fund Analysis
- Generate Investment Insights
- Create Interactive Dashboards
- Support Data-Driven Investment Decisions

---

## 👨‍💻 Internship Information

**Organization:** BlueStock Fintech

**Role:** Data Analyst Intern

**Project:** Mutual Fund Analytics Capstone

**Year:** 2026

---

## 🚀 Final GitHub Sync

After updating the project files, push the latest changes:

```bash
git add .
git commit -m "Day 4: Completed performance analytics and updated project documentation"
git push origin main
```

---

## 📜 License

This project is developed for educational and internship purposes as part of the BlueStock Fintech Data Analyst Internship Program.