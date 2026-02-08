# Credit Card Fraud Detection

## 📌 Problem Description

Credit card fraud causes significant financial losses for banks and customers.
The goal of this project is to build a **machine learning model that detects fraudulent credit card transactions** based on transaction-level features.

Given a transaction, the model predicts whether it is **fraudulent or legitimate**, allowing financial institutions to:

* Automatically block suspicious transactions
* Reduce financial losses
* Minimize inconvenience to legitimate customers

This is a **binary classification problem** with a highly imbalanced target variable, making it a realistic and challenging machine learning task.

---

## ⚙️ Project Setup

This project uses the **Credit Card Fraud Detection Dataset** from Kaggle, originally released by ULB.

### Dataset description

* The dataset contains **~285,000 credit card transactions** made by European cardholders.
* The target variable `Class` indicates whether a transaction is fraudulent (`1`) or legitimate (`0`). I later changed this variable's name to 'fraud'.
* Fraudulent transactions represent **~0.17%** of the data, resulting in a highly imbalanced classification problem.
* Features `V1`–`V28` are **PCA-transformed variables** to protect sensitive information.
* The `Amount` feature represents the transaction amount.

Due to GitHub file size limits, the dataset is **not included** in this repository.

### Download the dataset

1. Install and authenticate the Kaggle CLI:
   [https://www.kaggle.com/docs/api](https://www.kaggle.com/docs/api)

2. From the project root, run:

```bash
./download_data.sh
```

---

## 🐍 Python Environment

The project uses a `pyproject.toml` with **optional dependency groups** to clearly separate concerns.

### Dependency groups

* **repo** → full development environment (EDA, training, experiments)
* **api** → minimal runtime dependencies for inference and deployment

### Local development environment

Using `uv` (recommended):

```bash
uv venv
uv pip install -e .[repo]
```

This installs all libraries required for data analysis, model training, and experimentation.

---

## 🧠 Approach

The project follows these steps:

### 1. Exploratory Data Analysis (EDA)

Key findings from the exploratory analysis:

* The dataset is **extremely imbalanced**, with fraudulent transactions accounting for ~0.17% of observations.
* Transaction features are already anonymized and standardized due to PCA transformation.
* Transaction amounts show different distribution patterns between fraudulent and non-fraudulent cases.
* Due to imbalance, accuracy is not a meaningful metric for model evaluation.

These findings guided the choice of evaluation metrics and modeling strategy.

### 2. Model Training & Evaluation

The following models are trained and compared:

* Logistic Regression
* Random Forest
* XGBoost

Because the dataset is highly imbalanced, models are evaluated using metrics suitable for fraud detection:

* ROC-AUC
* Precision
* Recall
* F1-score

Hyperparameter tuning is applied to tree-based models to improve performance.

### 3. Model Deployment

* The final model is exported as a serialized artifact (`model.bin`)
* Predictions are served via a FastAPI REST API
* The application is containerized using Docker
* The service can be deployed to the cloud using AWS Elastic Beanstalk

---

## 🚀 Running the API Locally (Docker)

The inference service is implemented using **FastAPI** and packaged as a Docker container.

### Build the Docker image

```bash
docker build -t fraud-api .
```

### Run the container

```bash
docker run -p 8080:8080 fraud-api
```

### Available endpoints

* `GET /health` — service health check
* `POST /predictions` — fraud probability prediction

FastAPI documentation is available at:

```
http://localhost:8080/docs
```

### API usage example

Example request:

```bash
curl -X POST http://localhost:8080/predictions \
  -H "Content-Type: application/json" \
  -d '{
    "v1": 0.1,
    "v2": -1.2,
    "v3": 0.3,
    "v4": 0.4,
    "v5": -0.5,
    "v6": 0.6,
    "v7": 0.7,
    "v8": -0.8,
    "v9": 0.9,
    "v10": 0.1,
    "v11": 0.2,
    "v12": -0.3,
    "v13": 0.4,
    "v14": 0.5,
    "v15": -0.6,
    "v16": 0.7,
    "v17": -0.8,
    "v18": 0.9,
    "v19": 0.1,
    "v20": -0.2,
    "v21": 0.3,
    "v22": -0.4,
    "v23": 0.5,
    "v24": 0.6,
    "v25": -0.7,
    "v26": 0.8,
    "v27": -0.9,
    "v28": 0.1,
    "amount": 123.45
  }'
```

Example response:

```json
{
  "probability": 0.02,
  "is_fraud": false,
  "threshold": 0.3
}
```

---

## ☁️ Cloud Deployment (AWS Elastic Beanstalk)

The Dockerized API can be deployed to AWS Elastic Beanstalk.

### Deploy

```bash
eb init
eb create fraud-api-env
```

Once deployed, the API is publicly accessible via the Elastic Beanstalk URL.

### Teardown (important)

To avoid unnecessary costs:

```bash
eb terminate fraud-api-env
```

---


## 📁 Project Structure

```text
credit-card-fraud-detection/
├── Dockerfile
├── pyproject.toml
├── uv.lock
├── notebooks/
│   ├── example_request.ipynb
│   └── notebook.ipynb (EDA and model selection notebook)
├── src/
│   ├── example_post_request.py
│   ├── model.bin
│   ├── payment_operations.py (example request script)
│   ├── predict.py (REST API)
│   └── train.py (for training the model)
└── README.md
```

---

## 🎯 Intended Use

This project demonstrates an **end-to-end machine learning workflow**, from data analysis and model training to production-ready deployment.

It is intended for educational and portfolio purposes, simulating how a fraud detection model could be integrated into a real-world transaction processing system.

---

## ⚠️ Known Limitations & Next Steps

**Current limitations:**

* The model is trained on historical, static data and does not account for concept drift.
* Feature representations are anonymized, limiting feature interpretability.
* A fixed classification threshold is used for fraud decisions.

**Potential improvements:**

* Implement threshold optimization based on business costs.
* Add model monitoring and alerting for performance degradation.
* Introduce online or periodic retraining pipelines.
* Secure the API with authentication and rate limiting for production use.
