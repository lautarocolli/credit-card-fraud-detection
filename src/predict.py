import pickle
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict

class TransactionData(BaseModel):
    model_config = ConfigDict(extra='forbid')

    v1: float
    v2: float
    v3: float
    v4: float
    v5: float
    v6: float
    v7: float
    v8: float
    v9: float
    v10: float
    v11: float
    v12: float
    v13: float
    v14: float
    v15: float
    v16: float
    v17: float
    v18: float
    v19: float
    v20: float
    v21: float
    v22: float
    v23: float
    v24: float
    v25: float
    v26: float
    v27: float
    v28: float
    amount: float

class FraudResponse(BaseModel):
    fraud_probability: float
    fraud: bool

app = FastAPI(title = 'fraud-prediction')