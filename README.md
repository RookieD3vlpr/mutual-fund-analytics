# 📈 Mutual Fund Analytics Capstone

## 📝 Project Overview
This repository contains the code, data pipelines, and analytical models for the **Mutual Fund Analytics Capstone Project**, developed as part of the BlueStock Fintech Data Analyst Internship.

The objective of this project is to build an end-to-end data analytics pipeline that extracts live mutual fund data, processes historical financial datasets, and generates actionable investment insights using Python, SQL, and interactive dashboards.

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
├── scripts/                 # Python ETL pipeline scripts (fetching, cleaning, loading)
├── sql/                     # PostgreSQL/SQLite schema and analytical queries
├── dashboard/               # Interactive dashboard assets (Power BI / Web App)
├── reports/                 # Final PDF reports, presentations, and findings
│
├── .gitignore
├── data_dictionary.md
├── requirements.txt
└── README.md
```

## 🛠️ Tech Stack & Tools

- **Programming:** Python 3
- **Data Manipulation:** NumPy, Pandas
- **Database Management:** SQLite, SQLAlchemy, SQL
- **Data Visualization:** Matplotlib, Seaborn (Upcoming)
- **Environment:** VS Code, Jupyter Notebook, Git/GitHub

## 🚀 Setup & Installation

```bash
git clone https://github.com/YOUR-USERNAME/mutual-fund-analytics.git
cd mutual-fund-analytics
pip install -r requirements.txt
```

### Run the ETL Pipeline

```bash
python scripts/live_nav_fetch.py
python scripts/data_cleaning.py
python scripts/db_loader.py
```

## 📊 Current Progress

- ✅ Day 1: Project Setup & ETL
- ✅ Day 2: Data Cleaning & SQL Database

Developed during the **2026 BlueStock Fintech Data Analyst Internship**.

## 🚀 Pushing the Update

```bash
git add README.md
git commit -m "Update README with Day 2 progress and new folder structure"
git push origin main
```
