import sqlite3
import tkinter as tk
from tkinter import messagebox

# Connect to the database
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Example function to check connection
def test_connection():
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        messagebox.showinfo("Connection Successful", f"Connected!\nTables: {tables}")
    except Exception as e:
        messagebox.showerror("Error", f"Connection failed: {e}")

# GUI setup
root = tk.Tk()
root.title("Inventory Management System")

test_button = tk.Button(root, text="Test DB Connection", command=test_connection)
test_button.pack(pady=20)

root.mainloop()

# Close the connection when app closes
conn.close()
