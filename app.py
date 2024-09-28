from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('xgboost_model.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')

@app.route('/data_visualization')
def data_visualization():
    return render_template('data_visualization.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict_manually():       
    if request.method == 'POST':
        # Collect data from form
        try:
            Air_temperature = float(request.form['Air_temperature'])
            Process_temperature = float(request.form['Process_temperature'])
            Rotational_speed = float(request.form['Rotational_speed'])
            Torque = float(request.form['Torque'])
            Tool_wear = float(request.form['Tool_wear'])
            Type = float(request.form['Type'])

            # Prepare data for prediction
            sample = np.array([[Type, Air_temperature, Process_temperature, Rotational_speed, Torque, Tool_wear]])
            prediction = model.predict(sample)[0]

            # Dictionary mapping numeric labels to failure types
            failure_type_mapping = {
                0: 'Heat Dissipation Failure',
                1: 'No Failure',
                2: 'Overstrain Failure',
                3: 'Power Failure',
                4: 'Random Failures',
                5: 'Tool Wear Failure'
            }

            # Get the type of failure prediction
            failure_type_prediction = failure_type_mapping[prediction]

            # Render prediction result via a template
            return render_template('predict.html', prediction=prediction, failure_type_prediction=failure_type_prediction)
        except ValueError:
            # Handle the error if input is not a float
            return render_template('index.html', error="Please enter valid inputs.")

    # For GET requests, just redirect to the home page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)