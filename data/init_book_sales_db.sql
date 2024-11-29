-- 5. Connect to MySQL and create a new database 'book_sales_db'.
-- 6. Create a 'books_sales' table with the relevant columns.
-- 7. Insert the preprocessed data into the 'books_sales' table.

CREATE DATABASE `book_sales_db`;

USE 'book_sales_db';

-- Create the 'books_sales' table
CREATE TABLE 'books_sales' (
    BookID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each book
    Title VARCHAR(100) NOT NULL,                    -- Title of the book
    Author VARCHAR(100) NOT NULL,                   -- Author of the book
    Genre VARCHAR(50) NOT NULL,                     -- Genre of the book
    Price DECIMAL(10, 2) NOT NULL,                  -- Price of the book
);


