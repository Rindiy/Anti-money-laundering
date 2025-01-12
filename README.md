# Fraud Detection System for Money Laundering

## Overview

This project is designed to detect suspicious transactions and identify potential money laundering activities using machine learning algorithms. The system processes transaction data to classify whether a transaction is likely to be involved in laundering.

## Features
- Preprocessing of transaction data to handle categorical and numerical variables.
- Balanced sampling to address class imbalance in the dataset.
- Machine learning model (Random Forest Classifier) for transaction classification.
- ROC-AUC evaluation for performance measurement.
- Example predictions to test the system.
- Saved models and encoders for deployment.

## Requirements
- Python 3.8+
- Libraries: 
  - `numpy`
  - `pandas`
  - `seaborn`
  - `matplotlib`
  - `scikit-learn`
  - `joblib`

## Dataset
- **Input File:** `/inputtt.csv` (Replace with your dataset path)
- **Structure:**
  - `Time`, `Date`: Transaction timestamp.
  - `Sender_account`, `Receiver_account`: IDs of the accounts involved.
  - `Amount`: Transaction amount.
  - `Payment_currency`, `Received_currency`: Currencies used.
  - `Sender_bank_location`, `Receiver_bank_location`: Bank locations.
  - `Payment_type`: Mode of payment.
  - `Laundering_type`: Suspected laundering methods.
  - `Is_laundering`: Target variable (1 for laundering, 0 otherwise).

## Preprocessing
1. **Data Cleaning:**
   - Removed duplicates and handled null values.
2. **Feature Selection:**
   - Excluded non-predictive features like `Time`, `Date`, `Sender_account`, `Receiver_account`.
3. **Encoding:**
   - Used OneHotEncoder to transform categorical features.
   - Saved encoder as `encoder.pkl`.

## Model Training
- Algorithm: Random Forest Classifier
- Parameters: 
  - `max_depth=10`
  - `n_estimators=50`
  - `random_state=42`
- Training Accuracy: **99.66%**
- Testing Accuracy: **99.53%**
- ROC-AUC Score: **0.9997**

## Evaluation
- Confusion Matrix:
  ```
  [[2985   15]
   [   9 2102]]
  ```
- Classification Report:
  ```
               precision    recall  f1-score   support
           0       1.00      0.99      1.00      3000
           1       0.99      1.00      0.99      2111
  ```

## Example Prediction
To test the model, you can provide a transaction example:
```python
example = {
    "amount": [1415.59],
    "Payment_currency": ["UK pounds"],
    "Received_currency": ["UK pounds"],
    "Sender_bank_location": ["UK"],
    "Receiver_bank_location": ["UK"],
    "Payment_type": ["Cash Deposit"],
    "Laundering_type": ["Normal_Plus_Mutual"]
}
```
Run the script to get the prediction.

## Deployment
- Saved Model: `money_laundering.pkl`
- Saved Encoder: `encoder.pkl`

## Visualization
- Confusion matrix heatmap for model evaluation.

## Usage
1. **Train the Model:**
   Run the script to preprocess data, train the model, and save it.
2. **Predict New Transactions:**
   Load the saved model and encoder to classify new transactions.

