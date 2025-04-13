import sqlite3
import tkinter as tk
from tkinter import ttk

# Connect to the database
conn = sqlite3.connect("C:\Intro to Database Systems\Project 1\Application\CS665-Project-1\inventory.db")
cursor = conn.cursor()

# Create the main window
root = tk.Tk()
root.title("Inventory Management System")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

product_frame = tk.Frame(notebook)
notebook.add(product_frame, text="Products")

# Product Form Labels and Entries
tk.Label(product_frame, text="Name").grid(row=0, column=0)
tk.Label(product_frame, text="Stock").grid(row=1, column=0)
tk.Label(product_frame, text="Price").grid(row=2, column=0)

name_entry = tk.Entry(product_frame)
stock_entry = tk.Entry(product_frame)
price_entry = tk.Entry(product_frame)

name_entry.grid(row=0, column=1)
stock_entry.grid(row=1, column=1)
price_entry.grid(row=2, column=1)

# Treeview for displaying products
product_tree = ttk.Treeview(product_frame, columns=("ID", "Name", "Stock", "Price"), show="headings")
product_tree.heading("ID", text="ID")
product_tree.heading("Name", text="Name")
product_tree.heading("Stock", text="Stock")
product_tree.heading("Price", text="Price")

product_tree.grid(row=5, column=0, columnspan=4, pady=10)

def refresh_products():
    product_tree.delete(*product_tree.get_children())
    cursor.execute("SELECT * FROM Products")
    for row in cursor.fetchall():
        product_tree.insert('', 'end', values=row)

def add_product():
    name = name_entry.get()
    stock = int(stock_entry.get())
    price = float(price_entry.get())
    cursor.execute("INSERT INTO Products (Name, StockQuantity, Price) VALUES (?, ?, ?)", (name, stock, price))
    conn.commit()
    refresh_products()

def select_product(event):
    selected = product_tree.selection()
    if selected:
        values = product_tree.item(selected[0], 'values')
        name_entry.delete(0, tk.END)
        name_entry.insert(0, values[1])
        stock_entry.delete(0, tk.END)
        stock_entry.insert(0, values[2])
        price_entry.delete(0, tk.END)
        price_entry.insert(0, values[3])


def update_product():
    selected = product_tree.selection()
    if selected:
        product_id = product_tree.item(selected[0], 'values')[0]
        name = name_entry.get()
        stock = int(stock_entry.get())
        price = float(price_entry.get())
        cursor.execute("UPDATE Products SET Name=?, StockQuantity=?, Price=? WHERE ProductID=?",
                       (name, stock, price, product_id))
        conn.commit()
        refresh_products()

def delete_product():
    selected = product_tree.selection()
    if selected:
        product_id = product_tree.item(selected[0], 'values')[0]
        cursor.execute("DELETE FROM Products WHERE ProductID=?", (product_id,))
        conn.commit()
        refresh_products()

# Buttons
tk.Button(product_frame, text="Add Product", command=add_product).grid(row=3, column=0, pady=5)
tk.Button(product_frame, text="Update Product", command=update_product).grid(row=6, column=0, padx=5)
tk.Button(product_frame, text="Delete Product", command=delete_product).grid(row=6, column=1, padx=5)

product_tree.bind('<<TreeviewSelect>>', select_product)

# Initialize Treeview with data
refresh_products()

# Run the application
root.mainloop()
