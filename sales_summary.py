import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. CONNECT TO DATABASE (or create it if it doesn't exist)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# 2. CREATE SALES TABLE IF NOT EXISTS
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# 3. INSERT SAMPLE DATA (only if empty)
cursor.execute("SELECT COUNT(*) FROM sales")
if cursor.fetchone()[0] == 0:
    sample_data = [
        ("Apple", 10, 2.5),
        ("Banana", 20, 1.5),
        ("Orange", 15, 2.0),
        ("Apple", 5, 2.5),
        ("Banana", 10, 1.5),
        ("Orange", 10, 2.0)
    ]
    cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
    conn.commit()

# 4. RUN SQL QUERY TO GET SALES SUMMARY
query = """
SELECT 
    product, 
    SUM(quantity) AS total_quantity, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df = pd.read_sql_query(query, conn)

# 5. PRINT THE SUMMARY
print("=== SALES SUMMARY ===")
print(df)

# 6. PLOT BAR CHART OF REVENUE PER PRODUCT
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Save chart as image
plt.show()

# 7. CLOSE CONNECTION
conn.close()
