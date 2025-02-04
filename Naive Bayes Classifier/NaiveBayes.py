class NaiveBayesClassifier:
    def __init__(self):
        self.probabilities = {}
        self.class_probabilities = {}

    def fit(self, data, labels):
        unique_classes = set(labels)
        total_samples = len(labels)

        for cls in unique_classes:
            self.class_probabilities[cls] = labels.count(cls) / total_samples

        for cls in unique_classes:
            self.probabilities[cls] = {}
            class_indices = [i for i, label in enumerate(labels) if label == cls]
            class_data = [data[i] for i in class_indices]

            for feature_index in range(len(data[0])):
                values = [row[feature_index] for row in class_data]
                unique_values = set(values)
                self.probabilities[cls][feature_index] = {
                    value: values.count(value) / len(class_data) for value in unique_values
                }

    def predict(self, sample):
        class_scores = {}

        for cls in self.class_probabilities:
            class_scores[cls] = self.class_probabilities[cls]

            for feature_index in range(len(sample)):
                feature_value = sample[feature_index]
                if feature_value in self.probabilities[cls][feature_index]:
                    class_scores[cls] *= self.probabilities[cls][feature_index][feature_value]
                else:
                    class_scores[cls] *= 0

        return max(class_scores, key=class_scores.get)


#DATASET
default_data = [
    ["Sunny", "Hot", "High", "Weak"],
    ["Sunny", "Hot", "High", "Strong"],
    ["Overcast", "Hot", "High", "Weak"],
    ["Rainy", "Mild", "High", "Weak"],
    ["Rainy", "Cool", "Normal", "Weak"],
    ["Rainy", "Cool", "Normal", "Strong"],
    ["Overcast", "Cool", "Normal", "Strong"],
    ["Sunny", "Mild", "High", "Weak"],
    ["Sunny", "Cool", "Normal", "Weak"],
    ["Rainy", "Mild", "Normal", "Weak"],
    ["Sunny", "Mild", "Normal", "Strong"],
    ["Overcast", "Mild", "High", "Strong"],
    ["Overcast", "Hot", "Normal", "Weak"],
    ["Rainy", "Mild", "High", "Strong"]
]

default_labels = ["Yes", "No", "Yes", "Yes", "Yes", "No", "No", "Yes", "Yes", "Yes", "No", "No", "Yes", "No"]

nb = NaiveBayesClassifier()
nb.fit(default_data, default_labels)

while True:
    print("\nOPTIMAL DECISION PICKER FOR PLAYING BADMINTON")
    print("Enter the data you have for the weather:\n")

    test_outlook = input("Outlook (Sunny/Overcast/Rainy): ").strip()
    test_temperature = input("Temperature (Hot/Mild/Cool): ").strip()
    test_humidity = input("Humidity (High/Normal): ").strip()
    test_wind = input("Wind (Weak/Strong): ").strip()

    test_sample = [test_outlook, test_temperature, test_humidity, test_wind]

    prediction = nb.predict(test_sample)
    print(f"\nPrediction: {prediction}")

    terminate = input("\nWould you like to predict something again? (yes/no): ").strip().lower()
    if terminate != "yes":
        print("Thank you for using this DECISION MAKER")
        break