import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle

# 1. Load a dataset and split it into training and testing sets (80/20 or 70/30 split).
# 2. Train a Decision Tree classifier using the training data.
# 3. Evaluate the trained model using accuracy, precision, recall, and F1 score on the test data.
# 4. Save the trained model to a .pkl file for later use.
# 5. Ensure proper exception handling for data loading, model training, and evaluation.
# 6. Include meaningful error messages when the model cannot be trained or the evaluation fails (e.g., empty dataset, invalid data).

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")
    
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
    
def train_model(X_train, y_train):
    try:
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        raise Exception(f"Error training model: {str(e)}")
    
def evaluate_model(model, X_test, y_test):
    try:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        return accuracy, precision, recall, f1
    except Exception as e:
        raise Exception(f"Error evaluating model: {str(e)}")

def save_model(model, file_path):
    try:
        with open(file_path, 'wb') as file:
            pickle.dump(model, file)
        print(f"Model saved to {file_path}")
    except Exception as e:
        raise Exception(f"Error saving model: {str(e)}")
    

if __name__ == "__main__":
    file_path = r"C:\Users\david\BathUni\MA50290_24\programming-for-data-science-mock-exam\data\book_sales_transformed.csv"
    try:
        # Load data
        data = load_data(file_path)

        column_names = ['asin', 'title', 'author', 'productURL', 'stars', 'price',
            'isKindleUnlimited', 'category_id', 'isBestSeller', 'isEditorsPick',
            'isGoodReadsChoice', 'category_name']
        
        print("Available columns: " + ", ".join(column_names))

        input_columns = input("Enter the column to target for the model: ")

        if input_columns not in column_names:
            raise ValueError("Invalid column name. Please choose from the following columns: " + ", ".join(column_names))
        elif data[input_columns].nunique() <= 1:
            raise ValueError("Target column has only one unique value. Cannot train model.")
        elif data[input_columns].isnull().sum() > 0:
            raise ValueError("Target column contains missing values. Cannot train model.")
        else:
            print(f"Training model to predict: {input_columns}")
        
            # Split data
            X_train, X_test, y_train, y_test = split_data(data, target_column=input_columns)

        
            # Train model
            model = train_model(X_train, y_train)
        
            # Evaluate model
            accuracy, precision, recall, f1 = evaluate_model(model, X_test, y_test)
        
            print(f"Accuracy: {accuracy}")
            print(f"Precision: {precision}")
            print(f"Recall: {recall}")
            print(f"F1 Score: {f1}")
        
            # Save model
            save_model(model, "model.pkl")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
