# 🚗 Car Sales Prediction using Machine Learning and Flask

**🔖 Project Overview**

This project predicts the car purchase amount a customer is likely to spend based on personal and financial attributes. It integrates a machine learning model with a sleek Flask web interface to offer real-time predictions in a user-friendly manner.

**🎯 Problem Statement**

Car dealerships and automotive businesses need accurate insights into how much a potential customer can spend on a car. This project aims to provide such insights using historical data and predictive modeling.

**🧠 Machine Learning Approach**

Features Used:

Country

Gender

Age

Annual Salary

Credit Card Debt

Net Worth

Target: Car Purchase Amount

**Steps:**

Data Cleaning & Preprocessing (encoding, scaling)

Model Training using Linear Regression

Model Evaluation (MSE, R² Score)

Model Serialization using joblib

🌐 Web Integration (Flask)

Frontend: HTML + CSS with modern animated form

Backend: Flask

User fills out a form with input values

Inputs are encoded and scaled

Model predicts car purchase amount

Prediction is shown dynamically on the UI

**📄 Project Structure**
```
car-sales-predictor/
├── static/
├── templates/
│   └── index.html
├── model/
│   ├── sales_prediction_model.pkl
│   ├── scaler.pkl
│   ├── gender_encoder.pkl
│   └── country_encoder.pkl
├── app.py
├── requirements.txt
└── README.md
```

**📊 Sample Output**

Input: Male, USA, Age 45, Salary $85,000, Credit Card Debt $10,000, Net Worth $200,000Predicted Car Purchase Amount: $58,540.30

**🚀 Future Enhancements**

Add user login and history tracking

Use advanced models (XGBoost, ANN)

Deploy on Heroku / AWS / Render

Add database support for storing predictions

**💡 Tech Stack**

Python, Flask

Scikit-learn, Pandas, NumPy

HTML, CSS

Joblib

**📦 Requirements**

Install dependencies using:

pip install -r requirements.txt

**💼 Author**

Mohammad Mazid

B.Tech in Artificial Intelligence and Data Science

Passionate about AI, Web Development, and Problem Solving


