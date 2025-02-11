data = [
    (40, 20, "Red"),
    (50, 50, "Blue"),
    (60, 90, "Blue"),
    (10, 25, "Red"),
    (70, 70, "Blue"),
    (60, 10, "Red"),
    (25, 80, "Blue")
]

def sqrt(n, precision=0.00001):
    guess = n
    while abs(guess * guess - n) > precision:
        guess = (guess + n / guess) / 2
    return guess

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def knn_classify(new_point, k):
    distances = [(euclidean_distance(new_point, (x, y)), label) for x, y, label in data]
    
    distances.sort(key=lambda x: x[0])

    neighbors = distances[:k]

    class_count = {}
    for _, label in neighbors:
        class_count[label] = class_count.get(label, 0) + 1

    return max(class_count, key=class_count.get)

brightness = int(input("Enter Brightness: "))
saturation = int(input("Enter Saturation: "))
k = int(input("Enter number of neighbors (k): "))

predicted_class = knn_classify((brightness, saturation), k)

print(f"The predicted class for Brightness = {brightness}, Saturation = {saturation} is {predicted_class}.")