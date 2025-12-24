# FlexiMart – Data Warehouse and Analytics (Part 3)

## 📌 Overview
To analyze historical sales performance and enable business intelligence reporting, FlexiMart requires a **data warehouse** designed using dimensional modeling principles. This part of the project focuses on building a **star schema**, loading analytical data, and writing **OLAP-style queries** to support management decision-making.

The data warehouse separates transactional processing from analytical workloads, enabling fast aggregations, trend analysis, and drill-down reporting.

---

## 🎯 Objectives
- Design a star schema suitable for sales analytics
- Implement dimension and fact tables in a data warehouse
- Load realistic analytical data
- Write OLAP queries for time, product, and customer analysis

---

## 🧩 Task 3.1: Star Schema Design Documentation (10 Marks)

### 📄 File: `star_schema_design.md`

This document explains the star schema using **textual descriptions** and includes three sections:

### 🔹 Section 1: Schema Overview
- Describes the **fact table (`fact_sales`)** and its grain  
  *(one row per product per order line item)*
- Documents all **measures** such as quantity sold, unit price, discount, and total amount
- Explains all **dimension tables**:
  - `dim_date` – time-based analysis
  - `dim_product` – product attributes and categories
  - `dim_customer` – customer demographics and segmentation

Each table is clearly documented with purpose, keys, and attributes.

---

### 🔹 Section 2: Design Decisions
Explains:
- Why transaction line-item level granularity was chosen
- Why surrogate keys are used instead of natural keys
- How the schema supports **drill-down** and **roll-up** analysis  
  *(Year → Quarter → Month, Category → Product)*

---

### 🔹 Section 3: Sample Data Flow
Demonstrates how a single sales transaction flows from:
- Source system (order, customer, product)
- Into dimension tables
- And finally into the fact table

This section shows clear understanding of dimensional modeling.

---

## 🛠️ Task 3.2: Star Schema Implementation (10 Marks)

### 📄 Files
- `warehouse_schema.sql`
- `warehouse_data.sql`

### 🗃️ Schema Implementation
The warehouse schema is implemented **exactly as provided**, using:
- One fact table (`fact_sales`)
- Three dimension tables (`dim_date`, `dim_product`, `dim_customer`)
- Proper primary and foreign key constraints

---

### 📦 Data Loading Guidelines
The warehouse data meets all minimum requirements:

| Table | Requirement |
|-----|-------------|
| `dim_date` | 30 dates (Jan–Feb 2024, weekdays & weekends) |
| `dim_product` | 15 products across 3 categories |
| `dim_customer` | 12 customers across 4 cities |
| `fact_sales` | 40 realistic sales transactions |

Data values are realistic, varied, and free of foreign key violations.

---

## 📊 Task 3.3: OLAP Analytics Queries (15 Marks)

### 📄 File: `analytics_queries.sql`

This file contains three analytical SQL queries written for business stakeholders.

---

### 🔹 Query 1: Monthly Sales Drill-Down
**Business Scenario:**  
The CEO wants to analyze sales starting at the yearly level and drilling down to quarterly and monthly totals for 2024.

**Demonstrates:**
- Time-based aggregation
- Drill-down capability
- Use of date dimension attributes

---

### 🔹 Query 2: Product Performance Analysis
**Business Scenario:**  
The product manager wants to identify the **top 10 products by revenue** and understand their contribution to overall sales.

**Demonstrates:**
- Revenue and quantity aggregation
- Ranking and top-N logic
- Revenue contribution percentage using window functions or subqueries

---

### 🔹 Query 3: Customer Segmentation Analysis
**Business Scenario:**  
Marketing wants to segment customers into High, Medium, and Low value groups based on total spending.

**Demonstrates:**
- Customer-level aggregation
- CASE-based segmentation
- Grouped analysis with average revenue metrics

---

## 📦 Deliverables Summary

| File Name | Description |
|---------|------------|
| `star_schema_design.md` | Star schema documentation and design justification |
| `warehouse_schema.sql` | Data warehouse schema (provided, unchanged) |
| `warehouse_data.sql` | Dimension and fact table insert statements |
| `analytics_queries.sql` | OLAP queries for business analysis |

---

## 📊 Evaluation Focus
- Correct dimensional modeling concepts
- Proper fact and dimension table design
- Realistic and consistent analytical data
- Accurate OLAP queries with correct aggregations
- Clear documentation and professional formatting

---

## ✅ Outcome
By completing this part, FlexiMart gains:
- A scalable sales data warehouse
- Fast analytical querying capability
- Clear insights into time trends, product performance, and customer value
- A foundation for dashboards and advanced analytics

---

📌 **Note:** This data warehouse builds on cleaned transactional data from Part 1 and complements the NoSQL analysis in Part 2 as part of a hybrid data architecture.
