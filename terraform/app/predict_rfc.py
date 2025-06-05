import pandas as pd
import joblib

model = joblib.load("models/rfc_failure_model.pkl")

def predict_rfc_failure(payload: dict):
    df = pd.DataFrame([payload])
    prediction = model.predict(df)[0]
    return {"RFC_Failure_Predicted": bool(prediction)}
