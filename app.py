from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('filename.pkl')

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
            Type_L = float(request.form['Type_L'])
            Type_M = float(request.form['Type_M'])

            # Prepare data for prediction
            sample = np.array([[Air_temperature, Process_temperature, Rotational_speed, Torque, Tool_wear, Type_L, Type_M]])
            prediction = model.predict(sample)[0]

            # Render prediction result via a template
            return render_template('predict.html', prediction=prediction)
        except ValueError:
            # Handle the error if input is not a float
            return render_template('index.html', error="Please enter valid inputs.")

    # For GET requests, just redirect to the home page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
