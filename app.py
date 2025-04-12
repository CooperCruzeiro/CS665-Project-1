import tkinter as tk
from tkinter import ttk
import sqlite3

# Connect to the database
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create the main window
root = tk.Tk()
root.title("Inventory Management System")
root.geometry("900x600")

# Create notebook (tabs)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Create frames for each tab
tabs = {}
for table in ['Products', 'Suppliers', 'Customers', 'Transactions', 'Queries']:
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=table)
    tabs[table] = frame

# Placeholder for now - confirm GUI opens with tabs
root.mainloop()
