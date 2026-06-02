# 🎓 Student Exam Score Predictor

A beginner-friendly Machine Learning project built with Python and Scikit-Learn that predicts a student's exam score based on habits and attendance.

## 📌 Overview

This project uses a Linear Regression model to estimate exam scores from:

* Study Hours per Day
* Sleep Hours per Day
* Social Media consume per day
* Exercise
* Attendance Percentage

It demonstrates the complete Machine Learning workflow:

* Data Loading
* Data Preprocessing
* Model Training
* Model Evaluation
* Score Prediction
* Data Visualization

---

## 🚀 Features

* Predict student exam scores
* Train a Linear Regression model
* Evaluate model performance using:

  * Mean Absolute Error (MAE)
  * R² Score
* Interactive user input
* Data visualization using Matplotlib
* Simple and beginner-friendly code structure

---

## 📂 Project Structure

```text
student-score-predictor/
│
├── graph.py
├── main.py
├── README.md
├── requirements.txt
└── student_data.csv
```

---

## 🛠 Technologies Used

* Python
* Pandas
* Scikit-Learn
* Matplotlib

---

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/nahiannir/student-score-predictor.git
cd student-score-predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Train the Model and Predict Scores

```bash
python main.py
```

### Example

```text
Study Hours per Day: 6
Sleep Hours per Day: 8
Social Media consumption (per day): 4
Exercise: Yes
Attendance Percentage: 90

Predicted Exam Score: 82.54
```

---

## 📊 Visualization

Run the graph script:

```bash
python graph.py
```

This displays a scatter plot showing the relationship between study hours and exam scores.

---

## 🧠 Machine Learning Workflow

1. Load dataset from CSV
2. Split data into training and testing sets
3. Train Linear Regression model
4. Evaluate model accuracy
5. Accept user input
6. Predict exam score

---

## 📈 Evaluation Metrics

### Mean Absolute Error (MAE)

Measures the average prediction error.

### R² Score

Measures how well the model explains the variation in scores.

A higher R² score indicates better performance.

---

## 🔮 Future Improvements

* Save trained model using Pickle
* GUI using Tkinter
* SQLite database integration
* Student account system
* Prediction history tracking
* Multiple ML model comparison
* Flask web application
* Interactive dashboard
* Dark mode interface

---

## 🎯 Learning Outcomes

By completing this project, you will learn:

* Data Analysis with Pandas
* Machine Learning Fundamentals
* Regression Algorithms
* Model Evaluation
* Data Visualization
* Python Project Organization
* GitHub Project Documentation

---

## 📜 License

This project is open-source and available under the MIT License.

---

### ⭐ If you found this project useful, consider giving it a star on GitHub!
