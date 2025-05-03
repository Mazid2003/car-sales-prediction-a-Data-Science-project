from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load saved model and encoders
model = joblib.load('sales_prediction_model.pkl')
scaler = joblib.load('scaler.pkl')
gender_encoder = joblib.load('gender_encoder.pkl')
country_encoder = joblib.load('country_encoder.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            # Get form inputs
            name = request.form.get('name')
            email = request.form.get('email')
            country = request.form.get('country')
            gender = request.form.get('gender')
            age = float(request.form.get('age'))
            salary = float(request.form.get('salary'))
            debt = float(request.form.get('debt'))
            net_worth = float(request.form.get('net'))

            # Validate gender and country
            if gender not in gender_encoder.classes_:
                raise ValueError(f"Invalid gender: {gender}")
            if country not in country_encoder.classes_:
                raise ValueError(f"Invalid country: {country}")

            # Encode gender and country
            gender_encoded = gender_encoder.transform([gender])[0]
            country_encoded = country_encoder.transform([country])[0]

            # Prepare and scale features
            features = np.array([[country_encoded, gender_encoded, age, salary, debt, net_worth]])
            scaled_features = scaler.transform(features)

            # Make prediction
            predicted_amount = model.predict(scaled_features)[0]
            prediction = round(predicted_amount, 2)

        except Exception as e:
            print("Error during prediction:", e)
            prediction = "Error in input data."

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
