import pickle
import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel, ConfigDict

class Transaction(BaseModel):
    model_config = ConfigDict(extra='forbid')
    v1: float; v2: float; v3: float; v4: float; v5: float; v6: float
    v7: float; v8: float; v9: float; v10: float; v11: float; v12: float
    v13: float; v14: float; v15: float; v16: float; v17: float; v18: float
    v19: float; v20: float; v21: float; v22: float; v23: float; v24: float
    v25: float; v26: float; v27: float; v28: float
    amount: float

class Assessment(BaseModel):
    probability: float
    is_fraud: bool
    threshold: float = 0.3

# --- App Setup ---

app = FastAPI(
    title='Fraud Detection Service',
    version='1.0.0',
    description='REST API for transaction risk assessment'
)

with open('model.bin', 'rb') as f_in:
    model = pickle.load(f_in)

# --- Endpoints ---

@app.get("/health", status_code=status.HTTP_200_OK, tags=["System"])
def get_health():

    return {"status": "healthy"}

@app.post(
    "/predictions", 
    response_model=Assessment, 
    status_code=status.HTTP_201_CREATED,
    tags=["Predictions"]
)
def create_prediction(transaction: Transaction):

    features = list(transaction.model_dump().values())
    fraud_proba = model.predict_proba([features])[0, 1]
    
    threshold = 0.3
    return Assessment(
        probability=fraud_proba,
        is_fraud=bool(fraud_proba >= threshold),
        threshold=threshold
    )

@app.get("/")
def root():
    return {
        "message": "Credit Card Fraud Detection API",
        "FastAPI docs": "/docs",
        "health": "/health",
        "predict": "/predict"
    }

if __name__ == "__main__":
    uvicorn.run("predict:app", host="0.0.0.0", port=8080)