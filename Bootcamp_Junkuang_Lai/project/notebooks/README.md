# Demonstration research to interpret NVDA's future trends
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Individual investors often face challenges in analyzing stock price trends and making informed, data-driven predictions due to a lack of tools and expertise. This project aims to tackle this issue by developing a reproducible pipeline that automates the collection, cleaning, and analysis of daily stock data for Nvidia (NVDA) for the year 2023. The objective is to identify historical price patterns, detect anomalies, and create a regression model to predict future prices, enabling more informed investment decisions.

## Stakeholder & User
Stakeholder: Retail investors, financial bloggers, and educators seeking to empower individuals with better stock analytics,etc.
User: Individual investors who want to track, analyze, and forecast Nvidia stock performance as part of their investment workflow. Users interact with the output via notebooks, dashboards, or reports, typically before making buy/sell/hold decisions.

## Useful Answer & Decision
The project will identify historically profitable strategies through backtesting. While past performance does not guarantee future success, these strategies serve as predictive models.
Deliverables Include:
Quantitative performance metrics
Comparative performance charts

## Assumptions & Constraints
Assumptions:
Historical pricing data is accurate and reliable.
Constraints:
Time: Limited to a 2-week bootcamp (live trading not feasible).
Data: Dependent on CursorAI API's available stock price history.

## Known Unknowns / Risks
Historical Bias: Backtested success ≠ future profitability.
Data Limitations: Restricted to accessible market data.

## Lifecycle Mapping
Goal → Stage → Deliverable
+ Model problem with objective → Problem Framing & Scoping (Stage 01) → Data dictionary & methodology doc
+ Constracture project environment → Tooling Setup (Stage 02) → yfinance collector with error handling, .gitignore, .env.example
+ Achieve fundamental data-analyzing tools → Python Fundamentals (Stage 03) → Notebook with: momentum detection, sectoral decomposition
+ Collect and store reliable stock data → Data Acquisition/Ingestion (Stage 04) → Raw CSV file
+ Organize and validate data → Data Storage (Stage 05) → Raw/processed folders, format checks
+ Clean and prepare data → Data Preprocessing (Stage 06) → Cleaning scripts, visual comparison
+ Detect anomalies → Outlier Analysis (Stage 07) → Outlier report, boxplots

## Repo Plan
/data/raw/, /data/processed/: Store raw and cleaned stock data (CSV/Parquet)
/src/: Acquisition, cleaning, and utility scripts (e.g., acquisition.py, cleaning.py, utils.py, outliers.py, etc.)
/notebooks/: Jupyter notebooks for each project stage (acquisition, cleaning, EDA, regression, etc.)
/docs/: Project documentation and slides
.gitignore, .env.example: Ensure secrets and local configs are not committed

Update Cadence: Weekly during bootcamp, or as new features/data sources are added

## Data Cleaning Strategy
Use a modular and reproducible pipeline for data cleaning, implemented in src/cleaning.py:
Filling missing values: Numeric columns are filled with the median (robust to outliers).
Dropping columns: Columns with >50% missing values are dropped.
Scaling: Numeric features are scaled to [0, 1] for comparability.
Outlier detection: IQR method is used to flag or remove extreme values.
Visual comparison: Distributions and missingness are visualized before and after cleaning. All cleaning steps are implemented as reusable functions, ensuring transparency and reproducibility for future datasets.
