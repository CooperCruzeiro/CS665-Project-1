import sqlite3
import tkinter as tk
from tkinter import ttk

# Connect to the database
conn = sqlite3.connect("C:\Intro to Database Systems\Project 1\Application\CS665-Project-1\inventory.db")
cursor = conn.cursor()

# Create the main window
root = tk.Tk()
root.title("Inventory Management System")

# Create a Notebook widget to support tabbed views in the GUI
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

#---------------------------
# PRODUCTS TAB

# Create a frame for the Products tab
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

# Function to refresh and display all products in the Treeview
def refresh_products():
    product_tree.delete(*product_tree.get_children())
    cursor.execute("SELECT * FROM Products")
    for row in cursor.fetchall():
        product_tree.insert('', 'end', values=row)

# Function to add a new product to the database
def add_product():
    name = name_entry.get()
    stock = int(stock_entry.get())
    price = float(price_entry.get())
    cursor.execute("INSERT INTO Products (Name, StockQuantity, Price) VALUES (?, ?, ?)", (name, stock, price))
    conn.commit()
    refresh_products()

# Function to populate the entry fields when a Treeview item is selected
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

# Function to update an existing product in the database
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

# Function to delete a selected product from the database
def delete_product():
    selected = product_tree.selection()
    if selected:
        product_id = product_tree.item(selected[0], 'values')[0]
        cursor.execute("DELETE FROM Products WHERE ProductID=?", (product_id,))
        conn.commit()
        refresh_products()

# Buttons for user actions: add, update, and delete productstk.Button(product_frame, text="Add Product", command=add_product).grid(row=3, column=0, pady=5)
tk.Button(product_frame, text="Add Product", command=add_product).grid(row=3, column=0, pady=5)
tk.Button(product_frame, text="Update Product", command=update_product).grid(row=6, column=0, padx=5)
tk.Button(product_frame, text="Delete Product", command=delete_product).grid(row=6, column=1, padx=5)

# Bind Treeview selection event to function that fills form fields
product_tree.bind('<<TreeviewSelect>>', select_product)

# Load and display all products when app launches
refresh_products()


#---------------------------
# CUSTOMERS TAB

customer_frame = tk.Frame(notebook)
notebook.add(customer_frame, text="Customers")

# Customer Form Labels and Entry Fields
tk.Label(customer_frame, text="Name").grid(row=0, column=0)
tk.Label(customer_frame, text="Email").grid(row=1, column=0)
tk.Label(customer_frame, text="Address").grid(row=2, column=0)

cust_name_entry = tk.Entry(customer_frame)
cust_email_entry = tk.Entry(customer_frame)
cust_phone_entry = tk.Entry(customer_frame)

cust_name_entry.grid(row=0, column=1)
cust_email_entry.grid(row=1, column=1)
cust_phone_entry.grid(row=2, column=1)

# Treeview to display customers
customer_tree = ttk.Treeview(customer_frame, columns=("ID", "Name", "Email", "Address"), show="headings")
customer_tree.heading("ID", text="ID")
customer_tree.heading("Name", text="Name")
customer_tree.heading("Email", text="Email")
customer_tree.heading("Address", text="Address")
customer_tree.grid(row=5, column=0, columnspan=4, pady=10)

# Refresh the customer list
def refresh_customers():
    customer_tree.delete(*customer_tree.get_children())
    cursor.execute("SELECT * FROM Customers")
    for row in cursor.fetchall():
        customer_tree.insert('', 'end', values=row)

# Insert a new customer into the database
def add_customer():
    name = cust_name_entry.get()
    email = cust_email_entry.get()
    address = cust_phone_entry.get()
    cursor.execute("INSERT INTO Customers (Name, Email, Address) VALUES (?, ?, ?)", (name, email, address))
    conn.commit()
    refresh_customers()

# Populate entry fields with data from the selected customer row
def select_customer(event):
    selected = customer_tree.selection()
    if selected:
        values = customer_tree.item(selected[0], 'values')
        cust_name_entry.delete(0, tk.END)
        cust_name_entry.insert(0, values[1])
        cust_email_entry.delete(0, tk.END)
        cust_email_entry.insert(0, values[2])
        cust_phone_entry.delete(0, tk.END)
        cust_phone_entry.insert(0, values[3])

# Update the selected customer in the database
def update_customer():
    selected = customer_tree.selection()
    if selected:
        customer_id = customer_tree.item(selected[0], 'values')[0]
        name = cust_name_entry.get()
        email = cust_email_entry.get()
        address = cust_phone_entry.get()
        cursor.execute("UPDATE Customers SET Name=?, Email=?, Address=? WHERE CustomerID=?",
                       (name, email, address, customer_id))
        conn.commit()
        refresh_customers()

# Delete the selected customer from the database
def delete_customer():
    selected = customer_tree.selection()
    if selected:
        customer_id = customer_tree.item(selected[0], 'values')[0]
        cursor.execute("DELETE FROM Customers WHERE CustomerID=?", (customer_id,))
        conn.commit()
        refresh_customers()

# Buttons for Customer actions
tk.Button(customer_frame, text="Add Customer", command=add_customer).grid(row=3, column=0, pady=5)
tk.Button(customer_frame, text="Update Customer", command=update_customer).grid(row=6, column=0, padx=5)
tk.Button(customer_frame, text="Delete Customer", command=delete_customer).grid(row=6, column=1, padx=5)

customer_tree.bind('<<TreeviewSelect>>', select_customer)
refresh_customers()


#---------------------------
# SUPPLIERS TAB

supplier_frame = tk.Frame(notebook)
notebook.add(supplier_frame, text="Suppliers")

# Supplier Form Labels and Entry Fields
tk.Label(supplier_frame, text="Name").grid(row=0, column=0)
tk.Label(supplier_frame, text="Email").grid(row=1, column=0)
tk.Label(supplier_frame, text="Location").grid(row=2, column=0)

supp_name_entry = tk.Entry(supplier_frame)
supp_email_entry = tk.Entry(supplier_frame)
supp_location_entry = tk.Entry(supplier_frame)

supp_name_entry.grid(row=0, column=1)
supp_email_entry.grid(row=1, column=1)
supp_location_entry.grid(row=2, column=1)

# Treeview to display suppliers
supplier_tree = ttk.Treeview(supplier_frame, columns=("ID", "Name", "Email", "Location"), show="headings")
supplier_tree.heading("ID", text="ID")
supplier_tree.heading("Name", text="Name")
supplier_tree.heading("Email", text="Email")
supplier_tree.heading("Location", text="Location")
supplier_tree.grid(row=5, column=0, columnspan=4, pady=10)

# Refresh supplier list
def refresh_suppliers():
    supplier_tree.delete(*supplier_tree.get_children())
    cursor.execute("SELECT * FROM Suppliers")
    for row in cursor.fetchall():
        supplier_tree.insert('', 'end', values=row)

# Add supplier
def add_supplier():
    name = supp_name_entry.get()
    email = supp_email_entry.get()
    Location = supp_location_entry.get()
    cursor.execute("INSERT INTO Suppliers (Name, ContactInfo, Location) VALUES (?, ?, ?)", (name, email, Location))
    conn.commit()
    refresh_suppliers()

# Populate supplier fields on selection
def select_supplier(event):
    selected = supplier_tree.selection()
    if selected:
        values = supplier_tree.item(selected[0], 'values')
        supp_name_entry.delete(0, tk.END)
        supp_name_entry.insert(0, values[1])
        supp_email_entry.delete(0, tk.END)
        supp_email_entry.insert(0, values[2])
        supp_location_entry.delete(0, tk.END)
        supp_location_entry.insert(0, values[3])

# Update supplier
def update_supplier():
    selected = supplier_tree.selection()
    if selected:
        supplier_id = supplier_tree.item(selected[0], 'values')[0]
        name = supp_name_entry.get()
        email = supp_email_entry.get()
        Location = supp_location_entry.get()
        cursor.execute("UPDATE Suppliers SET Name=?, ContactInfo=?, Location=? WHERE SupplierID=?",
                       (name, email, Location, supplier_id))
        conn.commit()
        refresh_suppliers()

# Delete supplier
def delete_supplier():
    selected = supplier_tree.selection()
    if selected:
        supplier_id = supplier_tree.item(selected[0], 'values')[0]
        cursor.execute("DELETE FROM Suppliers WHERE SupplierID=?", (supplier_id,))
        conn.commit()
        refresh_suppliers()

# Buttons for Supplier actions
tk.Button(supplier_frame, text="Add Supplier", command=add_supplier).grid(row=3, column=0, pady=5)
tk.Button(supplier_frame, text="Update Supplier", command=update_supplier).grid(row=6, column=0, padx=5)
tk.Button(supplier_frame, text="Delete Supplier", command=delete_supplier).grid(row=6, column=1, padx=5)

supplier_tree.bind('<<TreeviewSelect>>', select_supplier)
refresh_suppliers()


# ---------------------
# Transactions Tab UI

transaction_frame = tk.Frame(notebook)
notebook.add(transaction_frame, text="Transactions")

# Transaction Form Labels and Entry Fields
tk.Label(transaction_frame, text="Product ID").grid(row=0, column=0)
tk.Label(transaction_frame, text="Quantity Change").grid(row=1, column=0)
tk.Label(transaction_frame, text="Transaction Date").grid(row=2, column=0)
tk.Label(transaction_frame, text="Customer ID").grid(row=3, column=0)

trans_product_entry = tk.Entry(transaction_frame)
trans_quantity_entry = tk.Entry(transaction_frame)
trans_date_entry = tk.Entry(transaction_frame)
trans_customer_entry = tk.Entry(transaction_frame)

trans_product_entry.grid(row=0, column=1)
trans_quantity_entry.grid(row=1, column=1)
trans_date_entry.grid(row=2, column=1)
trans_customer_entry.grid(row=3, column=1)

# Treeview to display transactions
transaction_tree = ttk.Treeview(transaction_frame, columns=("ID", "ProductID", "QuantityChange", "TransactionDate", "CustomerID"), show="headings")
transaction_tree.heading("ID", text="ID")
transaction_tree.heading("ProductID", text="Product ID")
transaction_tree.heading("QuantityChange", text="Quantity Change")
transaction_tree.heading("TransactionDate", text="Transaction Date")
transaction_tree.heading("CustomerID", text="Customer ID")
transaction_tree.grid(row=5, column=0, columnspan=4, pady=10)

# Refresh transaction list
def refresh_transactions():
    transaction_tree.delete(*transaction_tree.get_children())
    cursor.execute("SELECT * FROM Transactions")
    for row in cursor.fetchall():
        transaction_tree.insert('', 'end', values=row)

# Add transaction
def add_transaction():
    product_id = trans_product_entry.get()
    quantity_change = trans_quantity_entry.get()
    transaction_date = trans_date_entry.get()
    customer_id = trans_customer_entry.get()
    
    cursor.execute("INSERT INTO Transactions (ProductID, QuantityChange, TransactionDate, CustomerID) VALUES (?, ?, ?, ?)", 
                  (product_id, quantity_change, transaction_date, customer_id))
    
    # Update product stock quantity
    cursor.execute("UPDATE Products SET StockQuantity = StockQuantity + ? WHERE ProductID = ?", 
                  (quantity_change, product_id))
    
    conn.commit()
    refresh_transactions()
    refresh_products()  # Also refresh products to show updated stock

# Populate transaction fields on selection
def select_transaction(event):
    selected = transaction_tree.selection()
    if selected:
        values = transaction_tree.item(selected[0], 'values')
        trans_product_entry.delete(0, tk.END)
        trans_product_entry.insert(0, values[1])
        trans_quantity_entry.delete(0, tk.END)
        trans_quantity_entry.insert(0, values[2])
        trans_date_entry.delete(0, tk.END)
        trans_date_entry.insert(0, values[3])
        trans_customer_entry.delete(0, tk.END)
        trans_customer_entry.insert(0, values[4])

# Update transaction
def update_transaction():
    selected = transaction_tree.selection()
    if selected:
        transaction_id = transaction_tree.item(selected[0], 'values')[0]
        old_quantity = int(transaction_tree.item(selected[0], 'values')[2])
        
        product_id = trans_product_entry.get()
        new_quantity = int(trans_quantity_entry.get())
        transaction_date = trans_date_entry.get()
        customer_id = trans_customer_entry.get()
        
        # Calculate the difference for inventory adjustment
        quantity_difference = new_quantity - old_quantity
        
        cursor.execute("UPDATE Transactions SET ProductID=?, QuantityChange=?, TransactionDate=?, CustomerID=? WHERE TransactionID=?",
                      (product_id, new_quantity, transaction_date, customer_id, transaction_id))
        
        # Update product stock based on the quantity difference
        cursor.execute("UPDATE Products SET StockQuantity = StockQuantity + ? WHERE ProductID = ?", 
                      (quantity_difference, product_id))
        
        conn.commit()
        refresh_transactions()
        refresh_products()  # Also refresh products to show updated stock

# Delete transaction
def delete_transaction():
    selected = transaction_tree.selection()
    if selected:
        transaction_id = transaction_tree.item(selected[0], 'values')[0]
        product_id = transaction_tree.item(selected[0], 'values')[1]
        quantity_change = int(transaction_tree.item(selected[0], 'values')[2])
        
        # Reverse the quantity change in the product stock
        cursor.execute("UPDATE Products SET StockQuantity = StockQuantity - ? WHERE ProductID = ?",
                      (quantity_change, product_id))
        
        cursor.execute("DELETE FROM Transactions WHERE TransactionID=?", (transaction_id,))
        conn.commit()
        refresh_transactions()
        refresh_products()  # Also refresh products to show updated stock

# Buttons for Transaction actions
tk.Button(transaction_frame, text="Add Transaction", command=add_transaction).grid(row=4, column=0, pady=5)
tk.Button(transaction_frame, text="Update Transaction", command=update_transaction).grid(row=6, column=0, padx=5)
tk.Button(transaction_frame, text="Delete Transaction", command=delete_transaction).grid(row=6, column=1, padx=5)

transaction_tree.bind('<<TreeviewSelect>>', select_transaction)
refresh_transactions()



# Run the main GUI loop
root.mainloop()
