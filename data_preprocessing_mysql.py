import pandas as pd
import mysql.connector

# 1. Load the dataset 'book_sales.csv' into a pandas DataFrame.
# 2. Handle missing values (e.g., impute or remove rows/columns with missing data).
# 3. Normalize numerical columns (e.g., 'sales') using standard scaling or normalization techniques.
# 4. Encode categorical data (e.g., 'category' column) using one-hot encoding or label encoding.
# 5. Connect to MySQL and create a new database 'book_sales_db'.
# 6. Create a 'books_sales' table with the relevant columns.
# 7. Insert the preprocessed data into the 'books_sales' table.
# 8. Retrieve the top 5 books with the highest sales and display them in a user-friendly format.
# 9. Add proper exception handling for database connection, data loading, and insertion.
# 10. Ensure meaningful error messages for failed steps (e.g., database errors, missing columns).

