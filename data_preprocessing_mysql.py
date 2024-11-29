
import pandas as pd
import mysql.connector

# Load data
# TODO: Load 'data/book_sales.csv' into a DataFrame

# Preprocess data
# TODO: Handle missing values, normalize numerical columns, encode categorical data

# MySQL Connection
# TODO: Connect to MySQL and create 'book_sales_db' database and 'books_sales' table

# Insert data
# TODO: Insert preprocessed data into the MySQL table

# Query data
# TODO: Retrieve the top 5 books with the highest sales and display them


# Load data
df = pd.read_csv('data/book_sales.csv')

# Preprocess data
# Handle missing values
df.fillna(0, inplace=True)
