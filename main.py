# Student Exam Score Predictor
# Author: Nahian Nir
# Predicts a student's exam score using a Linear Regression model.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# =========================
# Load Dataset
# =========================

data = pd.read_csv("student_data.csv")

# Convert Exercise column to numeric values
data["Exercise"] = data["Exercise"].map({
    "Yes": 1,
    "No": 0
})

# =========================
# Features and Target
# =========================

X = data[
    [
        "StudyHours",
        "SleepHours",
        "Attendance",
        "SocialMediaConsume",
        "Exercise"
    ]
]

y = data["Score"]

# =========================
# Train/Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# Model Training
# =========================

model = LinearRegression()
model.fit(X_train, y_train)

# =========================
# Model Evaluation
# =========================

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("=" * 50)
print("🎓 STUDENT EXAM SCORE PREDICTOR")
print("=" * 50)

print(f"📊 Mean Absolute Error : {mae:.2f}")
print(f"📈 R² Score            : {r2:.2f}")

# =========================
# User Input
# =========================

print("\nEnter Student Details\n")

study_hours = float(input("📚 Study Hours per Day: "))
sleep_hours = float(input("😴 Sleep Hours per Day: "))
attendance = float(input("🏫 Attendance Percentage: "))
social_media = float(input("📱 Social Media Usage (Hours): "))

exercise = input("🏃 Exercise (Yes/No): ").strip().lower()

if exercise == "yes":
    exercise = 1
elif exercise == "no":
    exercise = 0
else:
    print("❌ Please enter Yes or No")
    exit()

# =========================
# Prediction
# =========================

user_data = pd.DataFrame({
    "StudyHours": [study_hours],
    "SleepHours": [sleep_hours],
    "Attendance": [attendance],
    "SocialMediaConsume": [social_media],
    "Exercise": [exercise]
})

predicted_score = model.predict(user_data)

print("\n" + "=" * 50)
print(f"🎯 Predicted Exam Score: {predicted_score[0]:.2f}")
print("=" * 50)

# Simple Feedback

if predicted_score[0] >= 85:
    print("🌟 Excellent Performance Expected!")
elif predicted_score[0] >= 70:
    print("👍 Good Performance Expected!")
elif predicted_score[0] >= 50:
    print("📚 Average Performance. More study may help.")
else:
    print("⚠️ Significant improvement needed.")