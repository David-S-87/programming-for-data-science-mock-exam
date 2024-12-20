import pandas as pd
import mysql.connector
from mysql.connector import Error
import pymysql
from pymysql import MySQLError
from getpass import getpass

from ml_test_package import (load_data,
                        data_preprocessing,
                        remove_duplicates,
                        one_hot_encode,
                        create_connection)

# 1. Load the dataset 'book_sales.csv' into a pandas DataFrame.
# 2. Handle missing values (e.g., impute or remove rows/columns with missing data).
# 3. Normalize numerical columns (e.g., 'sales') using standard scaling or normalization techniques.
# 4. Encode categorical columns if necessary.
# 5. Connect to MySQL and create a new database 'book_sales_db'.
# 6. Create a 'books_sales' table with the relevant columns.
# 7. Insert the preprocessed data into the 'books_sales' table.
# 8. Retrieve the top 5 books with the highest sales and display them in a user-friendly format.
# 9. Add proper exception handling for database connection, data loading, and insertion.
# 10. Ensure meaningful error messages for failed steps (e.g., database errors, missing columns).



# Database Functions

def create_table(cursor, table_name):
    try:
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            BookID INT AUTO_INCREMENT PRIMARY KEY,
            Title VARCHAR(255),
            Author VARCHAR(255),
            Genre VARCHAR(100),
            Price DECIMAL(10, 2)
        );
        """
        cursor.execute(create_table_query)
        print("Table created successfully (or already exists).")
    except MySQLError as e:
        print(f"Error: '{e}'")

def populate_database(data, cursor, table_name):
    try:
        insert_query = f"INSERT INTO {table_name} (Title, Author, Genre, Price) VALUES (%s, %s, %s, %s)"
        data_tuples = [tuple(x) for x in data[['title', 'author', 'category_name', 'price']].values]
        cursor.executemany(insert_query, data_tuples)
        connection.commit()
        print("Data inserted successfully.")
    except MySQLError as e:
        print(f"Error: '{e}'")

def retrieve_top_books(cursor, table_name, n=5):
    try:
        select_query = f"SELECT * FROM {table_name} ORDER BY Price DESC LIMIT {n}"
        cursor.execute(select_query)
        top_books = cursor.fetchall()
        print(f"Top {n} books with highest Price:")
        for i, book in enumerate(top_books):
            print(f"Book {i+1}: {book[1]} - Price: {book[4]}")
    except MySQLError as e:
        print(f"Error: '{e}'")



column_names = ['asin', 'title', 'author', 'productURL', 'stars', 'price',
       'isKindleUnlimited', 'category_id', 'isBestSeller', 'isEditorsPick',
       'isGoodReadsChoice', 'category_name']


# Main Execution
file_path = r"C:\Users\david\BathUni\MA50290_24\programming-for-data-science-mock-exam\data\book_sales.csv"
df = load_data(file_path)
df = remove_duplicates(df)

# Normalize relevant columns
# not required right now


# Encode categorical columns
# df = one_hot_encode(df, ['category_name'])

# Database interaction
connection = create_connection(database_name='book_sales_db')
if connection:
    cursor = connection.cursor()
    create_table(cursor, 'books_sales')
    populate_database(df, cursor, 'books_sales')
    retrieve_top_books(cursor, 'books_sales')
    connection.close()
    print("Connection to MySQL closed.")
else:
    print("Connection to MySQL failed.")



file_path = r"C:\Users\david\BathUni\MA50290_24\programming-for-data-science-mock-exam\data\book_sales.csv"

transformed_data = data_preprocessing(file_path)
# save the transformed data to a new file in the data folder
transformed_data.to_csv(r"C:\Users\david\BathUni\MA50290_24\programming-for-data-science-mock-exam\data\book_sales_transformed.csv", index=False)
