import pandas as pd
import joblib

model = joblib.load("models/auto_priority_model.pkl")

def predict_priority_tag(payload: dict):
    df = pd.DataFrame([payload])
    prediction = model.predict(df)[0]
    return {"Predicted_Priority": int(prediction)}
