from flask import Flask, request, jsonify, render_template 
from flask_cors import CORS
import pandas as pd
import xgboost as xgb
import pickle
import os

# Initialize Flask app
app = Flask(__name__,template_folder='templates',
           static_folder='static')
CORS(app)  # Enable CORS for all routes

# Get absolute path to model file
current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(os.path.dirname(current_dir), 'models')
model_path = os.path.join(model_dir, 'xgb_model.json')
print(model_path)
encoder_path = os.path.join(model_dir, 'label_encoders.pkl')
print(encoder_path)

# Create models directory if it doesn't exist
if not os.path.exists(model_dir):
    os.makedirs(model_dir)
    raise FileNotFoundError(f"Model directory created at {model_dir}. Please place xgb_model.model file here.")

# Check if model file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Load the trained model
try:
    model = xgb.Booster()
    model.load_model(model_path)
except Exception as e:
    raise Exception(f"Error loading model: {str(e)}")

# Load label encoders
try:
    with open(encoder_path, 'rb') as f:
        label_encoders = pickle.load(f)
except FileNotFoundError:
    raise FileNotFoundError("label_encoders.pkl not found in current directory")


# Route to render the frontend HTML
@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from POST request
        data = request.get_json()

        # Convert received data to a DataFrame
        data = {key: [value] for key, value in data.items()}
        df = pd.DataFrame(data)

        # Convert `Sender_account` and `Receiver_account` to numeric
        df['Sender_account'] = pd.to_numeric(df['Sender_account'], errors='coerce')
        df['Receiver_account'] = pd.to_numeric(df['Receiver_account'], errors='coerce')

        # Apply label encoding to categorical features
        for col, le in label_encoders.items():
            if col in df.columns:
                df[col] = le.transform(df[col])

        # Ensure all required columns are present in the correct order
        feature_columns = ['Sender_account', 'Receiver_account', 'Sender_bank_location', 
                           'Receiver_bank_location', 'Laundering_type']
        df = df[feature_columns]

        # Convert the DataFrame into DMatrix for prediction
        dmatrix = xgb.DMatrix(df)

        # Make predictions
        prediction = model.predict(dmatrix)
        prediction_binary = (prediction > 0.5).astype(int)

        # Return the prediction in a response
        return jsonify({'predictions': prediction_binary.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

    
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
