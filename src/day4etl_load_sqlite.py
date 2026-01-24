import sqlite3
import csv

# 1. Connect SQLite
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# 2. Create table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER, 
    price INTEGER, 
    quantity INTEGER
)               
""")

# 3. Load CSV into DB 
with open ("data/sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
         "INSERT INTO sales VALUES (?, ?, ?)",
         (row["order_id"], row["price"], row["quantity"])
        )
        
conn.commit()
conn.close()

print("SQLite ETL completed")