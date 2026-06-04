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
│   └── 03_eda_analysis.ipynb
│
├── scripts/                 # Python ETL pipeline scripts (fetching, cleaning, loading)
│
├── sql/                     # PostgreSQL/SQLite schema and analytical queries
│
├── dashboard/               # Interactive dashboard assets (Power BI / Web App)
│
├── reports/                 # Static charts, PDF reports, and presentations
│   ├── aum_growth_sbi.png
│   ├── category_inflow_heatmap.png
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

### Data Manipulation
- NumPy
- Pandas

### Database Management
- SQLite
- SQLAlchemy
- SQL

### Data Visualization
- Matplotlib
- Seaborn
- Plotly

### Environment
- VS Code
- Jupyter Notebook
- Git/GitHub

---

## 🚀 Setup & Installation

To run this project locally, follow these steps:

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

#### Fetch Live Data

```bash
python scripts/live_nav_fetch.py
```

#### Clean Historical Data

```bash
python scripts/data_cleaning.py
```

#### Load SQLite Database

```bash
python scripts/db_loader.py
```

### 4. View Exploratory Data Analysis

Open:

```text
notebooks/03_eda_analysis.ipynb
```

in **Jupyter Notebook** or **VS Code** to explore the complete EDA workflow and visualizations.

---

## 📊 Key Visualizations Generated

The EDA notebook generates the following insights and charts:

1. AUM Growth Analysis
2. SIP Inflow Trends
3. NAV Trend Analysis
4. NAV vs Returns Correlation
5. Investor Demographics Distribution
6. Geographic Investment Distribution
7. Category-wise Fund Inflow Heatmap
8. Sector Allocation Analysis
9. Risk vs Return Comparison
10. Mutual Fund Performance Dashboard

---

## 📈 Current Progress

### ✅ Day 1: Project Setup & ETL
- Configured development environment
- Built API extraction scripts
- Validated local CSV integrity

### ✅ Day 2: Data Cleaning & SQL Database
- Cleaned datasets using Pandas
- Designed Star Schema architecture
- Loaded data into SQLite
- Wrote analytical SQL queries

### ✅ Day 3: Exploratory Data Analysis (EDA)
- Completed deep-dive data analysis
- Generated 10 key financial insights
- Built interactive Plotly visualizations
- Created statistical analysis reports
- Produced business-ready charts and findings

### ⬜ Day 4: Dashboards & Final Reporting
- Building interactive dashboards
- Creating presentation-ready reports
- Finalizing project deliverables

---

## 🎯 Project Outcomes

By the end of this capstone project, the system will:

- Automate mutual fund data collection
- Maintain a structured financial database
- Generate actionable investment insights
- Provide interactive analytical dashboards
- Support data-driven investment decision-making

---

## 👨‍💻 Internship Project

Developed during the **2026 BlueStock Fintech Data Analyst Internship**.

---

## 🚀 Pushing the Update to GitHub

To lock in your completed Day 3 progress:

```bash
git add .
git commit -m "Day 3: Completed EDA Notebook, generated 10 insights, updated README"
git push origin main
```

---

### Repository Status

**Progress:** 75% Complete ✅

- ETL Pipeline → Completed
- Data Cleaning → Completed
- Database Design → Completed
- SQL Analytics → Completed
- Exploratory Data Analysis → Completed
- Dashboard Development → In Progress
- Final Reporting → In Progress