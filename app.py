import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Database Connection ---
conn = sqlite3.connect("C:\Intro to Database Systems\Project 1\Application\CS665-Project-1\inventory.db")
cursor = conn.cursor()

# --- Main Window Setup ---
root = tk.Tk()
root.title("Inventory Management System")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# --- Products Tab ---
products_tab = ttk.Frame(notebook)
notebook.add(products_tab, text="Products")

# --- Labels and Entry Widgets ---
labels = ["Product ID", "Name", "Price", "Stock Quantity", "Supplier ID"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(products_tab, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(products_tab)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label] = entry

# --- Treeview for Displaying Products ---
product_tree = ttk.Treeview(products_tab, columns=("ProductID", "Name", "Price", "StockQuantity", "SupplierID"), show="headings")
for col in product_tree["columns"]:
    product_tree.heading(col, text=col)
    product_tree.column(col, width=100)
product_tree.grid(row=0, column=3, rowspan=6, padx=10, pady=5)

# --- Functions ---
def refresh_products():
    product_tree.delete(*product_tree.get_children())
    cursor.execute("SELECT * FROM Products")
    for row in cursor.fetchall():
        product_tree.insert("", "end", values=row)

def add_product():
    try:
        product_data = (
            int(entries["Product ID"].get()),
            entries["Name"].get(),
            float(entries["Price"].get()),
            int(entries["Stock Quantity"].get()),
            int(entries["Supplier ID"].get())
        )
        cursor.execute("INSERT INTO Products (ProductID, Name, Price, StockQuantity, SupplierID) VALUES (?, ?, ?, ?, ?)", product_data)
        conn.commit()
        messagebox.showinfo("Success", "Product added successfully!")
        refresh_products()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add product: {e}")

# --- Buttons ---
tk.Button(products_tab, text="Add Product", command=add_product).grid(row=6, column=0, columnspan=2, pady=10)
tk.Button(products_tab, text="Refresh Table", command=refresh_products).grid(row=6, column=3, pady=10)

# Create frames for each tab
tabs = {}
for table in ['Suppliers', 'Customers', 'Transactions', 'Queries']:
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=table)
    tabs[table] = frame

# --- Initial Load ---
refresh_products()

root.mainloop()
