# Credit Card Fraud Detection

## 📌 Problem Description

Credit card fraud causes significant financial losses for banks and customers.  
The goal of this project is to build a **machine learning model that detects fraudulent credit card transactions** based on transaction-level features.

Given a transaction, the model predicts whether it is **fraudulent or legitimate**, allowing financial institutions to:

- Automatically block suspicious transactions  
- Reduce financial losses  
- Minimize inconvenience to legitimate customers  

This is a **binary classification problem** with a highly imbalanced target variable, making it a realistic and challenging machine learning task.

---

## Setting up the project

This project uses the **Credit Card Fraud Detection** dataset from Kaggle, originally released by ULB.

Due to GitHub file size limits, the dataset is **not included** in this repository.

### Download instructions

1. Install the Kaggle CLI and authenticate your account:
   https://www.kaggle.com/docs/api

2. From the project root, run:

   ```bash
   ./download_data.sh
   ```

### Jupyter setup

```bash
pip install jupyter ipykernel
python -m ipykernel install --user --name fraud-detection --display-name "Python (fraud-detection)"
jupyter notebook
```

## 🧠 Approach

The project follows these steps:

### 1. Exploratory Data Analysis (EDA)
- Analyze class imbalance
- Inspect feature distributions
- Study transaction amounts and timing
- Identify challenges related to fraud detection

### 2. Model Training & Evaluation
The following models are trained and compared:

- Logistic Regression (baseline)
- Random Forest
- XGBoost

Since the dataset is highly imbalanced, models are evaluated using metrics suitable for fraud detection:

- ROC-AUC
- Precision
- Recall
- F1-score

Hyperparameter tuning is applied to tree-based models to improve performance.

### 3. Model Deployment
- The final model is exported to a Python script
- Predictions are served via a REST API
- The application is packaged using Docker for reproducibility

---

## 🚀 Intended Use

The deployed service exposes an API endpoint that receives transaction features in JSON format and returns a fraud prediction.

This setup simulates how a fraud detection model could be integrated into a real-world transaction processing system.

---

## 📁 Project Structure