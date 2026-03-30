import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("AI-LAB10/cities.csv", header=None)
points = df.values

k = 3  # number of airports

# Initialize centers
np.random.seed(0)
centers = points[np.random.choice(len(points), k, replace=False)]

# Assign clusters
def assign_clusters(points, centers):
    clusters = [[] for _ in range(len(centers))]
    
    for p in points:
        distances = [np.linalg.norm(p - c) for c in centers]
        idx = np.argmin(distances)
        clusters[idx].append(p)
        
    return clusters

# Newton update
def update_centers_newton(clusters, centers, iterations=5):
    new_centers = []

    for i, cluster in enumerate(clusters):
        if len(cluster) == 0:
            new_centers.append(centers[i])
            continue

        x, y = centers[i]
        n = len(cluster)

        for _ in range(iterations):
            grad_x = sum(2*(x - p[0]) for p in cluster)
            grad_y = sum(2*(y - p[1]) for p in cluster)

            hessian = 2 * n

            x = x - grad_x / hessian
            y = y - grad_y / hessian

        new_centers.append([x, y])

    return np.array(new_centers)


def compute_cost(points, centers):
    cost = 0
    
    for i in range(len(points)):
        # squared distances to all centers
        distances = np.sum((points[i] - centers)**2, axis=1)
        
        # add minimum distance
        cost += np.min(distances)
    
    return cost

# Main loop
for iteration in range(20):
    clusters = assign_clusters(points, centers)
    centers = update_centers_newton(clusters, centers)
    
    cost = compute_cost(points, centers)
    print(f"Iteration {iteration+1}, Cost: {cost:.4f}")

# Final output
print("\nFinal Airport Locations:")
for i, c in enumerate(centers):
    print(f"Airport {i+1}: ({c[0]:.3f}, {c[1]:.3f})")

print("\nFinal Cost:", compute_cost(points, centers))


# import numpy as np
# import pandas as pd

# data = pd.read_csv("AI-LAB10/cities.csv", header=None)
# data.columns = ['x', 'y']
# points = data[['x', 'y']].values

# k = 3
# np.random.seed(42)
# centroids = points[np.random.choice(len(points), k, replace=False)]

# epochs = 20  # fewer iterations needed

# for epoch in range(epochs):
#     distances = np.linalg.norm(points[:, np.newaxis] - centroids, axis=2)
#     cluster_ids = np.argmin(distances, axis=1)

#     for i in range(k):
#         cluster_points = points[cluster_ids == i]
#         if len(cluster_points) == 0:
#             continue
        
#         # Newton step: mean of points (since Hessian = 2nI)
#         centroids[i] = np.mean(cluster_points, axis=0)

# # Compute cost
# cost = 0
# for i in range(len(points)):
#     cost += np.min(np.sum((points[i] - centroids) ** 2, axis=1))

# print("Newton Method Centroids:\n", centroids)
# print("Total Cost (SSD):", cost)