from fastapi import FastAPI
import torch
import numpy as np

app = FastAPI()

@app.post("/predict")
def predict():
    return {"predicted_price": round(np.random.uniform(250, 350), 2)}
