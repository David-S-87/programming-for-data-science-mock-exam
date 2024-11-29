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


