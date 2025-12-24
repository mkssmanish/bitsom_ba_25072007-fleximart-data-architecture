# FlexiMart – NoSQL Database Analysis (Part 2)

## 📌 Overview
As FlexiMart expands its product catalog, the company must support a wide variety of products with different attributes, frequent schema changes, and embedded customer feedback. Traditional relational databases become increasingly rigid under these requirements.

This part of the project evaluates **MongoDB as a NoSQL alternative**, explains why it is suitable for a dynamic product catalog, and demonstrates basic MongoDB operations using real product data.

The objective is to understand **when and why NoSQL databases are preferred**, and to implement practical MongoDB queries and aggregations.

---

## 🎯 Objectives
- Analyze limitations of relational databases for highly diverse product data
- Justify the use of MongoDB for flexible product catalogs
- Implement common MongoDB operations such as querying, updating, and aggregation
- Work with embedded documents and arrays (product specs and reviews)

---

## 🧩 Task 2.1: NoSQL Justification Report (Theory)

### 📄 File: `nosql_analysis.md`

The report is divided into three sections:

### 🔹 Section A: Limitations of RDBMS
Explains why relational databases struggle with:
- Products having different attributes (e.g., electronics vs fashion items)
- Frequent schema changes when introducing new product types
- Storing customer reviews as nested or hierarchical data

This section highlights schema rigidity, table alteration overhead, and complex joins.

---

### 🔹 Section B: NoSQL Benefits (MongoDB)
Explains how MongoDB addresses these challenges through:
- Flexible, schema-less document structure
- Embedded documents for product specifications and reviews
- Horizontal scalability using sharding

This section connects MongoDB features directly to FlexiMart’s business needs.

---

### 🔹 Section C: Trade-offs
Identifies disadvantages of using MongoDB instead of MySQL, such as:
- Lack of strong relational constraints
- Limited support for complex multi-table transactions

---

## 🛠️ Task 2.2: MongoDB Implementation (Practical)

### 📄 File: `mongodb_operations.js`

This file contains five MongoDB operations implemented using JavaScript syntax and well-commented for clarity.

### 📦 Sample Data
- File: `products_catalog.json`
- Contains 10 products across 2 categories
- Each product includes:
  - Basic attributes (name, category, price, stock)
  - Nested `specs` object
  - Embedded `reviews` array

---

### 🔧 Implemented Operations

#### ✅ Operation 1: Load Data
- Imports `products_catalog.json` into the `products` collection

#### ✅ Operation 2: Basic Query
- Retrieves Electronics products priced below ₹50,000
- Displays only name, price, and stock

#### ✅ Operation 3: Review Analysis
- Uses aggregation to calculate average ratings
- Filters products with average rating ≥ 4.0

#### ✅ Operation 4: Update Operation
- Adds a new customer review to an existing product
- Demonstrates update with embedded arrays

#### ✅ Operation 5: Complex Aggregation
- Calculates average product price per category
- Returns category name, average price, and product count
- Sorted by average price in descending order

---

## 📦 Deliverables Summary

| File Name | Description |
|---------|------------|
| `nosql_analysis.md` | Theory report explaining RDBMS limitations, NoSQL benefits, and trade-offs |
| `mongodb_operations.js` | MongoDB queries and aggregations with comments |
| `products_catalog.json` | Sample product data with nested structures |

---

## 📊 Evaluation Focus
- Clear understanding of relational vs NoSQL databases
- Correct use of MongoDB document model and aggregation framework
- Clean syntax, comments, and readable structure
- Practical alignment with real-world product catalog scenarios

---

## ✅ Outcome
By completing this part, FlexiMart gains:
- A scalable and flexible product catalog design
- Embedded customer reviews without complex joins
- Faster evolution of product data structures
- A strong foundation for future analytics and personalization

---

📌 **Note:** This part complements the relational ETL pipeline (Part 1) and demonstrates how hybrid data architectures can be used effectively in modern systems.
