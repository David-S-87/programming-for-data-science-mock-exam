# data_loader.py

import pandas as pd
import pymysql
from sklearn.preprocessing import StandardScaler
from pymysql import MySQLError
from getpass import getpass
from sklearn.model_selection import train_test_split

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")
    
def handle_missing_values(data):
    try:
        cleaned_data = data.dropna()
        return cleaned_data
    except Exception as e:
        raise Exception(f"Error handling missing values: {str(e)}")
    
def remove_duplicates(data):
    try:
        cleaned_data = data.drop_duplicates()
        return cleaned_data
    except Exception as e:
        raise Exception(f"Error removing duplicates: {str(e)}")
    
def normalize_data(data, columns):
    try:
        for col in columns:
            if col in data.columns:  # Check if column exists
                data[col] = (data[col] - data[col].mean()) / data[col].std()
            else:
                print(f"Column '{col}' not found in the data.")
        return data
    except Exception as e:
        raise Exception(f"Error normalizing data: {str(e)}")

def one_hot_encode(data, columns):
    try:
        encoded_data = pd.get_dummies(data, columns=columns)
        return encoded_data
    except Exception as e:
        raise Exception(f"Error encoding data: {str(e)}")
    

def data_preprocessing(file_path):
    try:
        # Load data
        df = load_data(file_path)
        # Remove duplicates
        df = remove_duplicates(df)
        # Handle missing values
        df = handle_missing_values(df)
        # Normalize numerical columns
        df = normalize_data(df, ['price'])
        # Encode categorical columns
        # df = one_hot_encode(df, ['category'])
        return df
    except Exception as e:
        raise Exception(f"Data preprocessing error: {str(e)}")




def split_data(data, target_column, test_size=0.2):
    try:
        X = data.drop(columns=[target_column])
        y = data[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        X_train = X_train.select_dtypes(include=[int, float])
        y_train = y_train.astype([int, float])
        X_test = X_test.select_dtypes(include=[int, float])
        y_test = y_test.astype([int, float])
        return X_train, X_test, y_train, y_test
    except Exception as e:
        raise Exception(f"Error splitting data: {str(e)}")
    

def standardize_data(X_train, X_test):
    try:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        return X_train, X_test
    except Exception as e:
        raise Exception(f"Error standardizing data: {str(e)}")
    

def create_connection(database_name='book_sales_db'):
    try:
        connection = pymysql.connect(
            host='localhost',
            user=input("Enter username: "),
            password=getpass("Enter password: "),
            database=database_name
        )
        print("Connection to MySQL established successfully.")
        return connection
    except MySQLError as e:
        print(f"Error: '{e}'")
        return None
    
