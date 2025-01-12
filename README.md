# **Fraud Detection System for Money Laundering**

This project is a Flask-based web application designed to predict fraudulent transactions and identify potential money laundering activities. It uses XGBoost for predictions in the Flask app, while a separate Random Forest model is implemented and evaluated in a standalone Jupyter notebook.

---

## **Features**
- **Frontend**: Interactive web interface for transaction input.
- **Backend**: Flask application serving predictions using the trained XGBoost model.
- **Random Forest**: A separate notebook for training and evaluation.
- **Data Preprocessing**: Label encoding for categorical variables and feature transformation.
- **API**: `/predict` endpoint for real-time fraud detection.
- **Modular Design**: Organized directory structure for ease of development and scalability.

---

## **Directory Structure**
```
Frontend/
├── app/
│   ├── templates/
│   │   └── index.html          # Frontend HTML file
│   ├── app.py                  # Flask application
├── data/
│   └── test.txt                # Sample test data
├── models/
│   ├── label_encoders.pkl      # Pickled label encoders
│   ├── xgb_model.json          # Trained XGBoost model
├── notebooks/
│   ├── Untitled4.ipynb         # XGBoost training notebook
│   └── Anti_money_laundering_Randomforest.ipynb # Random Forest notebook
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd Frontend
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Models**:
   - Train the XGBoost model using the dataset provided in the `notebooks/Untitled4.ipynb`.
   - Save the trained XGBoost model as `xgb_model.json`.
   - Save the label encoders as `label_encoders.pkl`.
   - Place these files in the `models/` directory.

4. **Run the Flask Application**:
   ```bash
   python app/app.py
   ```

5. **Access the Application**:
   - Open a browser and navigate to `http://127.0.0.1:5000/`.

---

## **Usage**

1. **Frontend**:
   - Access the web interface via the browser.
   - Enter transaction details like `Sender_account`, `Receiver_account`, etc.
   - Submit the form to get predictions.

2. **API**:
   - Use the `/predict` endpoint to send JSON data for prediction.
   - Example JSON format:
     ```json
     {
       "Sender_account": "12345",
       "Receiver_account": "67890",
       "Sender_bank_location": "Location_A",
       "Receiver_bank_location": "Location_B",
       "Laundering_type": "Type_X"
     }
     ```

---

## **Endpoints**
| **Endpoint** | **Method** | **Description**                              |
|--------------|------------|----------------------------------------------|
| `/`          | GET        | Renders the frontend HTML.                  |
| `/predict`   | POST       | Accepts JSON input and returns predictions. |

---

## **Model Details**
- **XGBoost**:
  - Trained using the dataset in the `notebooks/Untitled4.ipynb`.
  - Used for real-time fraud detection in the Flask application.
- **Random Forest**:
  - Trained and evaluated separately in the `notebooks/Anti_money_laundering_Randomforest.ipynb`.
  - Provides additional insights and serves as a benchmark model.
- **Preprocessing**:
  - Label encoding for categorical variables.
  - Numeric conversion for account IDs.

---

## **Acknowledgments**
- **Dataset**: [Anti Money Laundering Transaction Data (SAML-D)](https://www.kaggle.com/datasets).  

---
