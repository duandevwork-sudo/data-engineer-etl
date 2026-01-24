import sqlite3

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM sales")
print(cursor.fetchall())

conn.close()
