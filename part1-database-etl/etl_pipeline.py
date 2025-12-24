import pandas as pd
import mysql.connector
import re
from datetime import datetime
import os
from dotenv import load_dotenv

# 1. Load the .env file
load_dotenv()

# 2. Access the variables
HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DB_DATABASE")

# ---------------- DATABASE CONFIG ----------------
DB_CONFIG = {
    "host": HOST,
    "user": USER,
    "password": PASSWORD, 
    "database": DATABASE
}

DATA_PATH = "../data/"
report = []

# ---------------- HELPER FUNCTIONS ----------------
def log(msg):
    report.append(msg)

def standardize_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r"\D", "", str(phone))
    if len(digits) == 10:
        return f"+91-{digits}"
    return None

def parse_date(val):
    if pd.isna(val):
        return None

    val = str(val).strip()

    known_formats = [
        "%Y-%m-%d",   # 2024-01-15
        "%d/%m/%Y",   # 15/01/2024
        "%m/%d/%Y",   # 01/15/2024
        "%m-%d-%Y",   # 01-15-2024
        "%d-%m-%Y"    # 15-01-2024
    ]

    for fmt in known_formats:
        try:
            return datetime.strptime(val, fmt).date()
        except ValueError:
            continue

    # fallback (won't warn)
    try:
        return pd.to_datetime(val, errors="coerce").date()
    except:
        return None



# ---------------- EXTRACT ----------------
customers_df = pd.read_csv(DATA_PATH + "customers_raw.csv")
products_df = pd.read_csv(DATA_PATH + "products_raw.csv")
sales_df = pd.read_csv(DATA_PATH + "sales_raw.csv")

log(f"Customers extracted: {len(customers_df)}")
log(f"Products extracted: {len(products_df)}")
log(f"Sales extracted: {len(sales_df)}")

# ---------------- TRANSFORM : CUSTOMERS ----------------
customers_df.drop_duplicates(subset=["email"], inplace=True)
customers_df.dropna(subset=["email"], inplace=True)

customers_df["phone"] = customers_df["phone"].apply(standardize_phone)
customers_df["registration_date"] = customers_df["registration_date"].apply(parse_date)

log(f"Customers after cleaning: {len(customers_df)}")

# ---------------- TRANSFORM : PRODUCTS ----------------
products_df.drop_duplicates(subset=["product_name"], inplace=True)

products_df["category"] = products_df["category"].str.strip().str.title()
products_df["price"].fillna(products_df["price"].median(), inplace=True)
products_df["stock_quantity"].fillna(0, inplace=True)

log(f"Products after cleaning: {len(products_df)}")

# ---------------- TRANSFORM : SALES ----------------
sales_df.drop_duplicates(subset=["transaction_id"], inplace=True)
sales_df.dropna(subset=["customer_id", "product_id"], inplace=True)

sales_df["transaction_date"] = sales_df["transaction_date"].apply(parse_date)

log(f"Sales after cleaning: {len(sales_df)}")

# ---------------- LOAD ----------------
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()

# Clear existing data
cursor.execute("SET FOREIGN_KEY_CHECKS=0")
cursor.execute("TRUNCATE order_items")
cursor.execute("TRUNCATE orders")
cursor.execute("TRUNCATE customers")
cursor.execute("TRUNCATE products")
cursor.execute("SET FOREIGN_KEY_CHECKS=1")

# ---------------- LOAD CUSTOMERS (GENERATE INT IDs) ----------------
customer_id_map = {}

for _, row in customers_df.iterrows():
    cursor.execute("""
        INSERT INTO customers (first_name, last_name, email, phone, city, registration_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row["first_name"],
        row["last_name"],
        row["email"],
        row["phone"],
        row["city"],
        row["registration_date"]
    ))
    customer_id_map[row["customer_id"]] = cursor.lastrowid

log(f"Customers loaded: {len(customer_id_map)}")

# ---------------- LOAD PRODUCTS (GENERATE INT IDs) ----------------
product_id_map = {}

for _, row in products_df.iterrows():
    cursor.execute("""
        INSERT INTO products (product_name, category, price, stock_quantity)
        VALUES (%s, %s, %s, %s)
    """, (
        row["product_name"],
        row["category"],
        row["price"],
        row["stock_quantity"]
    ))
    product_id_map[row["product_id"]] = cursor.lastrowid

log(f"Products loaded: {len(product_id_map)}")

conn.commit()

# ---------------- LOAD ORDERS & ORDER_ITEMS ----------------
for _, row in sales_df.iterrows():
    raw_customer_id = row["customer_id"]
    raw_product_id = row["product_id"]

    if raw_customer_id not in customer_id_map or raw_product_id not in product_id_map:
        continue

    customer_int_id = customer_id_map[raw_customer_id]
    product_int_id = product_id_map[raw_product_id]

    total_amount = row["quantity"] * row["unit_price"]

    cursor.execute("""
        INSERT INTO orders (customer_id, order_date, total_amount, status)
        VALUES (%s, %s, %s, %s)
    """, (
        customer_int_id,
        row["transaction_date"],
        total_amount,
        row["status"]
    ))

    order_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        order_id,
        product_int_id,
        row["quantity"],
        row["unit_price"],
        total_amount
    ))

conn.commit()
cursor.close()
conn.close()

log("ETL pipeline completed successfully")

# ---------------- DATA QUALITY REPORT ----------------
with open("data_quality_report.txt", "w") as f:
    f.write("\n".join(report))
