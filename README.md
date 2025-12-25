# FlexiMart Data Architecture Project

**Student Name:** Manish Kumar Singh 

**Student ID:** bitsom_ba_25072007  

**Email:** mkssmanish@gmail.com 

**Date:** December 25, 2025

---

## Project Overview

This project implements a complete end-to-end **data architecture solution** for FlexiMart.  
It covers transactional data ingestion using an ETL pipeline, NoSQL-based product catalog analysis using MongoDB, and a dimensional data warehouse for advanced analytics and reporting.

The solution demonstrates how relational databases, NoSQL systems, and data warehouses work together to support operational processing and business intelligence needs.

---

## Repository Structure

```text
├── part1-database-etl/
│   ├── etl_pipeline.py
│   ├── schema_documentation.md
│   ├── business_queries.sql
│   └── data_quality_report.txt
├── part2-nosql/
│   ├── nosql_analysis.md
│   ├── mongodb_operations.js
│   └── products_catalog.json
├── part3-datawarehouse/
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│   └── analytics_queries.sql
└── README.md
```


## Technologies Used

- Python 3.x – ETL pipeline development
- pandas – Data cleaning and transformation
- MySQL 8.0 / PostgreSQL 14 – Relational database and data warehouse
- MongoDB 6.0 – NoSQL product catalog
- SQL – Business queries, OLAP analytics, window functions

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mkssmanish/bitsom_ba_25072007-fleximart-data-architecture.git
cd fleximart-data-architecture
```

### 2. Create and Activate Virtual Environment (Python)

#### On Linux / macOS

```pyhton
python3 -m venv venv
source venv/bin/activate
```
#### On Windows (PowerShell)

```python
python3 -m venv venv
venv\Scripts\activate
```

Once activated, your terminal prompt will show (venv).

### 3. Install Python Dependencies

Ensure requirements.txt exists in the root directory, then run:

```python
pip install --upgrade pip
pip install -r requirements.txt
```

Example requirements.txt:

- pandas
- mysql-connector-python
- python-dotenv

### 4. Environment Configuration (.env)

Create a .env file in the root directory to store database credentials securely:

- DB_HOST=YOUR_DB_HOST
- DB_PORT=YOUR_DB_PORT
- DB_DATABASE=DATABASE_NAME
- DB_USER=DATABASE_USER
- DB_PASSWORD=YOUR_MYSQL_PASSWORD

⚠️ Do not commit .env files to version control.

---

# Create databases

```bash
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

```

---

# Run Part 1 - ETL Pipeline

```python
python part1-database-etl/etl_pipeline.py

```

---

# Run Part 1 - Business Queries

```bash
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

```

---

# Run Part 3 - Data Warehouse

### Run Data Warehouse Schema

```bash
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql

```
### Load Data Warehouse Data

```bash
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql

```
### Run OLAP Analytics Queries
```bash
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql

```

---


# MongoDB Setup

```bash

mongosh < part2-nosql/mongodb_operations.js

```

---

# Key Learnings

- Implemented a robust ETL pipeline to clean and normalize real-world data

- Understood the trade-offs between relational and NoSQL databases

- Designed a star schema data warehouse for historical and analytical reporting

- Wrote OLAP queries using aggregations and window functions

---

# Challenges Faced
## 1. Inconsistent and Missing Data

- Solved using validation rules, standardization logic, and controlled default values.

## 2. Star Schema Design and Granularity Selection

- Addressed by selecting transaction-level granularity and using surrogate keys for all dimensions.