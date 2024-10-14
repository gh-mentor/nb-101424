/*
This file contains a script of Transact SQL (T-SQL) command to interact with a database named 'Inventory'.
Requirements:
- SQL Server 2022 is installed and running

Details:
- Check if the database 'Inventory' exists, if not, create it
- Sets the default database to 'Inventory'.
- Create a 'categories' table and related 'products' table.
- Remove all rows from the tables.
- Populate the 'categories' table with sample data.
- Populate the 'products' table with sample data.
- Create stored procedures to get all categories.
- Create a stored procedure to get all products in a specific category.
- Create a stored procudure to get all products in a specific price range sorted by price in ascending order.
*/

-- Check if the database 'Inventory' exists, if not, create it
IF NOT EXISTS (SELECT name FROM master.dbo.sysdatabases WHERE name = N'Inventory')
BEGIN
    CREATE DATABASE Inventory;
END
GO

-- Sets the default database to 'Inventory'.
USE Inventory;

-- Create a 'categories' table and related 'products' table.
CREATE TABLE categories
(
    id INT PRIMARY KEY,
    name NVARCHAR(50) NOT NULL
);

CREATE TABLE products
(
    id INT PRIMARY KEY,
    name NVARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category_id INT NOT NULL,
    -- add a created_at column to store the date and time when the product was created
    created_at DATETIME NOT NULL DEFAULT GETDATE(),
    -- add an updated_at column to store the date and time when the product was last updated
    updated_at DATETIME NOT NULL DEFAULT GETDATE(),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Remove all rows from the tables.
TRUNCATE TABLE categories;
TRUNCATE TABLE products;

-- Populate the 'categories' table with sample data.
INSERT INTO categories (id, name) VALUES (1, 'Electronics');
INSERT INTO categories (id, name) VALUES (2, 'Clothing');
INSERT INTO categories (id, name) VALUES (3, 'Books');
INSERT INTO categories (id, name) VALUES (4, 'Home & Kitchen');

-- Populate the 'products' table with sample data.
INSERT INTO products (id, name, price, category_id) VALUES (1, 'Laptop', 999.99, 1);
INSERT INTO products (id, name, price, category_id) VALUES (2, 'Smartphone', 599.99, 1);
INSERT INTO products (id, name, price, category_id) VALUES (3, 'T-shirt', 19.99, 2);
INSERT INTO products (id, name, price, category_id) VALUES (4, 'Jeans', 39.99, 2);
INSERT INTO products (id, name, price, category_id) VALUES (5, 'Novel', 9.99, 3);
INSERT INTO products (id, name, price, category_id) VALUES (6, 'Cooking Utensils Set', 49.99, 4);
INSERT INTO products (id, name, price, category_id) VALUES (7, 'Coffee Maker', 29.99, 4);

-- Create stored procedures to get all categories.
CREATE PROCEDURE GetAllCategories
AS
BEGIN
    SELECT * FROM categories;
END;
GO

-- Create a stored procedure to get all products in a specific category.
CREATE PROCEDURE GetProductsByCategory
    @category_id INT
AS
BEGIN
    SELECT * FROM products WHERE category_id = @category_id;
END;
GO

-- Create a stored procudure to get all products in a specific price range sorted by price in ascending order.
CREATE PROCEDURE GetProductsByPriceRange
    @min_price DECIMAL(10, 2),
    @max_price DECIMAL(10, 2)
AS
BEGIN
    SELECT * FROM products WHERE price BETWEEN @min_price AND @max_price ORDER BY price ASC;
END;
GO







