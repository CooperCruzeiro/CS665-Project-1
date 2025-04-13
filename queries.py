import sqlite3
import os
# Connect to the database
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Function to execute a SQL file
def execute_sql_file(filename):
    with open(filename, 'r') as file:
        sql_script = file.read()
        cursor.executescript(sql_script)
        print(f"Executed {filename} successfully.")

# Run the SQL scripts in order
try:
    execute_sql_file('create.sql')  # Creates the tables
    execute_sql_file('insert.sql')  # Inserts sample data
    execute_sql_file('crud.sql')    # Performs CRUD operations
except Exception as e:
    print(f"Error: {e}")

# Commit and close the connection
conn.commit()
conn.close()
print("All SQL scripts executed successfully.")