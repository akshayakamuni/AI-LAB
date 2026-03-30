import numpy as np
import pandas as pd

# Load data
data = pd.read_csv("AI-LAB10/cities.csv", header=None)
data.columns = ['x', 'y']  # assign column names
points = data[['x', 'y']].values  # assume columns x, y

k = 3  # number of airports

# Initialize centroids randomly
np.random.seed(42)
centroids = points[np.random.choice(len(points), k, replace=False)]

learning_rate = 0.01
epochs = 100

for epoch in range(epochs):
    # Assign clusters
    distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
    cluster_ids = np.argmin(distances, axis=1)

    # Update centroids using gradient descent
    for i in range(k):
        cluster_points = points[cluster_ids == i]
        if len(cluster_points) == 0:
            continue
        
        gradient = -2 * np.sum(cluster_points - centroids[i], axis=0)
        centroids[i] = centroids[i] - learning_rate * gradient / len(cluster_points)

# Compute total cost
cost = 0
for i in range(len(points)):
    cost += np.min(np.sum((points[i] - centroids) ** 2, axis=1))

print("Gradient Descent Centroids:\n", centroids)
print("Total Cost (SSD):", cost)