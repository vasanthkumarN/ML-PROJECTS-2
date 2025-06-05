import pandas as pd
import joblib

model = joblib.load("models/priority_model.pkl")

def predict_high_priority(payload: dict):
    df = pd.DataFrame([payload])
    prediction = model.predict(df)[0]
    return {"Is_High_Priority": int(prediction)}
