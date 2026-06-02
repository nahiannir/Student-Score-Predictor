# Student Score Predictor Visualization

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("student_data.csv")

# Convert Exercise column
data["Exercise"] = data["Exercise"].map({
    "Yes": 1,
    "No": 0
})

# Create Scatter Plot
plt.figure(figsize=(8, 5))

plt.scatter(
    data["StudyHours"],
    data["Score"]
)

plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)

plt.tight_layout()
plt.show()