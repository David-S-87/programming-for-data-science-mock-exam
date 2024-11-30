import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from ml_test_package import load_data, split_data
# 1. Define a simple feedforward neural network class using PyTorch (with at least one hidden layer).
# 2. Load the dataset and split it into training and testing sets.
# 3. Standardize the feature values before feeding them into the neural network.
# 4. Train the neural network on the training data and visualize the loss curve over epochs.
# 5. Add proper exception handling during data loading, model training, and evaluation (e.g., invalid data type, empty dataset).
# 6. Provide meaningful error messages when PyTorch dependencies are missing or installation fails.

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out
    
    
def train_model(model, X_train, y_train, num_epochs=100, learning_rate=0.001):
    try:
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)
        for epoch in range(num_epochs):
            inputs = torch.tensor(X_train, dtype=torch.float32)
            labels = torch.tensor(y_train.values, dtype=torch.long)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            if (epoch+1) % 10 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')
    except Exception as e:
        raise Exception(f"Error training model: {str(e)}")
    
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
            print(f"Training model with target column: {input_columns}")


            X_train, X_test, y_train, y_test = split_data(data, 'target')
            X_train, X_test = standardize_data(X_train, X_test)
            input_size = X_train.shape[1]
            hidden_size = 128
            num_classes = len(y_train.unique())
            model = NeuralNetwork(input_size, hidden_size, num_classes)
            train_model(model, X_train, y_train)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    