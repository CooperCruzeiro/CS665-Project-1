-- insert.sql

-- sample suppliers
INSERT INTO Suppliers (Name, ContactInfo, Location) VALUES ('ABC Supplies', 'abc@example.com', 'New York');
INSERT INTO Suppliers (Name, ContactInfo, Location) VALUES ('XYZ Wholesalers', 'xyz@example.com', 'Los Angeles');

-- sample products
INSERT INTO Products (Name, StockQuantity, Price, SupplierID) VALUES ('Laptop', '10', 999.99, 1);
INSERT INTO Products (Name, StockQuantity, Price, SupplierID) VALUES ('Chair', '20', 49.99, 2);

-- sample customers
INSERT INTO Customers (Name, Email, Address) VALUES ('John Doe', 'johndoe@example.com', '123 Elm St');
INSERT INTO Customers (Name, Email, Address) VALUES ('Jane Smith', 'janesmith@example.com', '456 Oak St');

-- sample transactions
INSERT INTO Transactions (ProductID, QuantityChange, TransactionDate, CustomerID) VALUES (1, -1, '2025-03-29', 1);
INSERT INTO Transactions (ProductID, QuantityChange, TransactionDate, CustomerID) VALUES (2, -2, '2025-03-29', 2);
