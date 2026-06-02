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
│   ├── raw/                 # Unaltered CSV files and fetched API data
│   └── processed/           # Cleaned and transformed datasets
│
├── notebooks/               # Jupyter notebooks for EDA
├── sql/                     # PostgreSQL scripts and queries
├── dashboard/               # Flask API and visualization assets
├── reports/                 # Final reports and presentations
│
├── .gitignore
├── data_ingestion.py
├── live_nav_fetch.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack & Tools

### Programming
- Python 3

### Data Analysis
- NumPy
- Pandas

### Data Visualization
- Matplotlib
- Seaborn
- Plotly

### Database
- PostgreSQL
- pgAdmin 4
- SQLAlchemy

### API Development
- Flask
- Requests

### Development Environment
- VS Code
- Jupyter Notebook

---

## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/mutual-fund-analytics.git
cd mutual-fund-analytics
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Fetch Live NAV Data

```bash
python live_nav_fetch.py
```

### 4. Validate Local Datasets

```bash
python data_ingestion.py
```

---

## 📊 Current Progress

- ✅ Day 1: Project Setup & ETL
  - Configured environment
  - Built API extraction scripts
  - Validated local CSV integrity

- ⬜ Day 2: Exploratory Data Analysis (EDA)
  - Data cleaning
  - Visualization using Pandas and Seaborn

- ⬜ Day 3: SQL & Database Integration
  - Load processed data into PostgreSQL
  - Develop business queries

- ⬜ Day 4: API & Visualization
  - Build Flask REST API
  - Serve analytical insights

---

## 🎯 Project Goals

- Automate mutual fund data collection
- Perform exploratory financial analysis
- Store and query data using PostgreSQL
- Build APIs for data access
- Create dashboards for investment insights

---

## 👨‍💻 Internship Project

Developed as part of the **2026 BlueStock Fintech Data Analyst Internship**.

---

## 📌 GitHub Update Commands

```bash
git add README.md
git commit -m "Update README with professional structure and project overview"
git push origin main
```
