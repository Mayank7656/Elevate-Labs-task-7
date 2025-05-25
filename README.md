# Elevate-Labs-task-7

# 🧾 Basic Sales Summary using SQLite and Python

This project is a simple sales analysis tool built with Python, SQLite, and Pandas. It creates a small local database, runs SQL queries to calculate total quantity sold and revenue per product, and visualizes the results with a bar chart.

---

## 🎯 Objective

To practice basic data analysis using:
- SQL queries embedded in Python
- SQLite for local storage
- Pandas for data handling
- Matplotlib for visualization

---

## 🛠 Tools Used

- Python 3.x
- SQLite (built into Python)
- Pandas
- Matplotlib

---

## 📁 Files Included

| File               | Description                                         |
|--------------------|-----------------------------------------------------|
| `sales_summary.py` | Main Python script that runs the entire analysis    |
| `sales_data.db`    | SQLite database file (auto-created by the script)   |
| `sales_chart.png`  | Bar chart image showing revenue per product         |

---

## 📦 How It Works

1. **Creates** a database called `sales_data.db` and a table `sales`
2. **Inserts sample data** into the table (if not already inserted)
3. **Runs SQL** to calculate:
   - Total quantity sold
   - Total revenue (quantity × price)
4. **Prints** the result as a summary table
5. **Generates a bar chart** of revenue per product

---

## 📊 Sample Output

=== SALES SUMMARY ===
product total_quantity revenue
0 Apple 15 37.5
1 Banana 30 45.0
2 Orange 25 50.0

And a bar chart is saved as `sales_chart.png`.

---

## ▶️ How to Run

### Step 1: Install Dependencies
`
pip install pandas matplotlib
`

### Step 2: Run the Script
`
python sales_summary.py
`

