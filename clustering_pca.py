import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# 1. Load the dataset into a pandas DataFrame.
# 2. Apply PCA (Principal Component Analysis) to reduce the data to 2 principal components.
# 3. Visualize the dataset after PCA reduction in 2D using Matplotlib.
# 4. Apply K-means clustering to the PCA-reduced data (choose the number of clusters appropriately).
# 5. Visualize the clusters using different colors in a scatter plot.
# 6. Add proper exception handling when loading the data, running PCA, and applying K-means clustering.
# 7. Include user input/output validation (e.g., number of clusters, dataset loading).


def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")
    
def apply_pca(data, n_components=2):
    try:
        # only apply PCA to numerical columns
        data = data.select_dtypes(include=[np.number])
        pca = PCA(n_components=n_components)
        pca_data = pca.fit_transform(data)
        return pca_data
    except Exception as e:
        raise Exception(f"Error applying PCA: {str(e)}")
    
def kmeans(data, n_clusters):
    try:
        kmeans = KMeans(n_clusters=n_clusters)
        kmeans.fit(data)
        return kmeans.labels_
    except Exception as e:
        raise Exception(f"Error applying K-means clustering: {str(e)}")
    
def visualize_clusters(data, labels):
    try:
        plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.title('K-means Clustering')
        plt.show()
    except Exception as e:
        raise Exception(f"Error visualizing clusters: {str(e)}")
    
if __name__ == "__main__":
    file_path = r"C:\Users\david\BathUni\MA50290_24\programming-for-data-science-mock-exam\data\book_sales_transformed.csv"
    try:
        number_of_clusters = int(input("Enter the number of clusters: "))
        if number_of_clusters <= 0:
            raise ValueError("Number of clusters should be greater than 0.")
        elif number_of_clusters > 10:
            raise ValueError("Number of clusters should not exceed 10.")
        elif number_of_clusters > 5:
            print("Warning: Using a large number of clusters may result in overfitting.")
        elif number_of_clusters == 1:
            print("Warning: Using only 1 cluster may not provide meaningful results.")
        elif type(number_of_clusters) != int:
            raise ValueError("Number of clusters should be an integer.")
        else:
            data = load_data(file_path)
            pca_data = apply_pca(data)
            labels = kmeans(pca_data, number_of_clusters)
            visualize_clusters(pca_data, labels)
    except Exception as e:
        print(f"An error occurred: {str(e)}")



    
