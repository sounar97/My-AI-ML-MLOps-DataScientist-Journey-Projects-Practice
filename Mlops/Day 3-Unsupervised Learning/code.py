# Import necessary libraries
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris()

# Create KMeans model
model = KMeans(n_clusters=3)

# Train model
model.fit(iris.data)