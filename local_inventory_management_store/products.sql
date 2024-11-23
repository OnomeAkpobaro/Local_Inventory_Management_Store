CREATE DATABASE IF NOT EXIST Store_Inventory;
USE Store_Inventory;
CREATE TABLE IF NOT EXIST Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    stock_quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
);