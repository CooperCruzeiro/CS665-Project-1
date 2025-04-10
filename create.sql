-- create.sql 


-- Drop tables if they already exist
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Transactions;

-- Suppliers Table
CREATE TABLE Suppliers (
    SupplierID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    ContactInfo TEXT,
    Location TEXT NOT NULL
);
-- Functional Dependency: SupplierID - (Name, ContactInfo, Location)

-- Products Table
CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    StockQuantity INTEGER NOT NULL,
    Price REAL NOT NULL,
    SupplierID INTEGER,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
);
-- Functional Dependency: ProductID - (Name, StockQuantity, Price, SupplierID)

-- Customers Table
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    ContactInfo TEXT,
    Address TEXT NOT NULL
);
-- Functional Dependency: CustomerID - (Name, ContactInfo, Address)

-- Transactions Table
CREATE TABLE Transactions (
    TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER NOT NULL,
    QuantityChange INTEGER NOT NULL,
    TransactionDate TEXT NOT NULL,
    CustomerID INTEGER,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
-- Functional Dependency: TransactionID - (ProductID, QuantityChange, TransactionDate, CustomerID)

