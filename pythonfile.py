import math

# List of points in 2D space
points = [(1, 2), (4, 6), (5, 8), (9, 10)]

# Function to calculate Euclidean distance between two points
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# List to store distances
distances = []

# Calculate distances between each pair of points
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Find the minimum distance
min_distance = min(distances)

# Print the minimum distance
print("The minimum distance is:", min_distance)