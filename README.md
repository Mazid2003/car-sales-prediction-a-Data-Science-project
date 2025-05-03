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
├── sales_prediction_model.pkl
├── scaler.pkl
├── gender_encoder.pkl
├── country_encoder.pkl
├── app.py
├── requirements.txt
└── README.md
```

**📊 Sample Output**

Input: Male, USA, Age 45, Salary $85,000, Credit Card Debt $10,000, Net Worth $200,000

Predicted Car Purchase Amount: $58,540.30

**How to run the project**

**1. Clone the repository**

git clone https://github.com/Mazid2003/car-sales-prediction-a-Data-Science-project.git

cd car_sales

**2. Install requirements**

pip install -r requirements.txt

**3. Run the Flask app**

python app.py

Then open your browser at http://127.0.0.1:5000/

**Screenshots**

![screenshot_2025-04-30_19-42-36](https://github.com/user-attachments/assets/1ef879a8-735a-4439-8b4a-2278d1220830)
![screenshot_2025-04-30_19-45-17](https://github.com/user-attachments/assets/b1311d3f-52ee-4ce7-844f-40163a072af2)
![screenshot_2025-04-30_19-44-48](https://github.com/user-attachments/assets/bfd5e4b2-e468-4f02-912c-c04b9d106606)

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


