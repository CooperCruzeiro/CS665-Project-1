-- crud.sql
sklfhjsahl
-- Create operations 
INSERT INTO Products (Name, StockQuantity, Price, SupplierID) VALUES ('Desk', 'Furniture', 79.99, 2);
INSERT INTO Suppliers (Name, ContactInfo, Location) VALUES ('LMN Distributors', 'lmn@example.com', 'Chicago');
INSERT INTO Customers (Name, ContactInfo, Address) VALUES ('Alice Brown', 'alice@example.com', '789 Pine St');
INSERT INTO Transactions (ProductID, QuantityChange, TransactionDate, CustomerID) VALUES (1, -1, '2025-03-29', 2);

-- Read operations 
SELECT * FROM Products
SELECT * FROM Suppliers;
SELECT * FROM Customers;
SELECT * FROM Transactions;

-- Update operations
UPDATE Products SET Price = 799.99 WHERE Name = 'Laptop';
UPDATE Suppliers SET ContactInfo = 'new_xyz@example.com' WHERE Name = 'XYZ Wholesalers';
UPDATE Customers SET ContactInfo = 'new_jane@example.com' WHERE Name = 'Jane Smith';
UPDATE Transactions SET TransactionDate = '2025-04-01' WHERE TransactionID = 1;

-- Delete operations 
DELETE FROM Products WHERE Name = 'Desk';
DELETE FROM Suppliers WHERE Name = 'LMN Distributors';
DELETE FROM Customers WHERE Name = 'Alice Brown';   
DELETE FROM Transactions WHERE TransactionID = 1;
