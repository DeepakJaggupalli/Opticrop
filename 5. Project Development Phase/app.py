from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained ML model
try:
    model = joblib.load('models/model.pkl')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tool')
def tool():
    return render_template('predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not found on server.'})
        
    try:
        data = request.json
        # Extract features
        N = float(data.get('N', 0))
        P = float(data.get('P', 0))
        K = float(data.get('K', 0))
        temperature = float(data.get('temperature', 0))
        humidity = float(data.get('humidity', 0))
        ph = float(data.get('ph', 0))
        rainfall = float(data.get('rainfall', 0))

        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        
        # Predict
        prediction = model.predict(features)
        
        return jsonify({
            'success': True,
            'prediction': prediction[0].capitalize()
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
