import pandas as pd

from ml_test_package import (data_preprocessing, 
                             split_data, 
                             standardize_data, 
                             train_model, 
                             evaluate_model)

# 1. Refactor the existing code into reusable, modular functions:
#    - A function for loading the dataset.
#    - A function for preprocessing the data (normalization, encoding).
#    - A function for training the model.
#    - A function for evaluating the model.
# 2. Ensure each function has a clear and descriptive docstring.
# 3. Properly structure the imports in this file (avoid loading major external packages in __init__.py).
# 4. Ensure that each function is reusable and easily testable in isolation.



# Main Execution
if __name__ == "__main__":
    file_path = r"C:\Users\david\BathUni\MA50290_24\programming-for-data-science-mock-exam\data\book_sales_transformed.csv"
    try:
        preprocessed_data = data_preprocessing(file_path)
        X_train, X_test, y_train, y_test = split_data(preprocessed_data)
        X_train, X_test = standardize_data(X_train, X_test)
        model = train_model(X_train, y_train)
        accuracy = evaluate_model(model, X_test, y_test)
        print(f"Model accuracy: {accuracy}")
    except Exception as e:
        print(f"An error occurred: {e}")

