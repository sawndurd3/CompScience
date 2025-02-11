data = [
    (15, 30),
    (22, 40),
    (35, 50),
    (50, 65),
    (65, 80),
    (80, 95),
    (90, 20),
    (55, 10),
    (42, 35),
    (77, 60)
]

def sqrt(n, precision=0.00001):
    guess = n
    while abs(guess * guess - n) > precision:
        guess = (guess + n / guess) / 2
    return guess

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def initialize_centroids(data, k):
    return data[:k]

def assign_clusters(data, centroids):
    clusters = {i: [] for i in range(len(centroids))}
    
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        closest_centroid = distances.index(min(distances))
        clusters[closest_centroid].append(point)
    
    return clusters

def compute_new_centroids(clusters):
    new_centroids = []
    
    for cluster_points in clusters.values():
        if cluster_points: 
            sum_x = sum(p[0] for p in cluster_points)
            sum_y = sum(p[1] for p in cluster_points)
            new_centroids.append((sum_x // len(cluster_points), sum_y // len(cluster_points)))
    
    return new_centroids

def kmeans(data, k, max_iterations=100):
    centroids = initialize_centroids(data, k)
    
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = compute_new_centroids(clusters)

        if new_centroids == centroids:
            break
        
        centroids = new_centroids

    return clusters


k = int(input("Enter the number of clusters (k): "))
final_clusters = kmeans(data, k)

for cluster_id, points in final_clusters.items():
    print(f"Cluster {cluster_id + 1}: {points}")
