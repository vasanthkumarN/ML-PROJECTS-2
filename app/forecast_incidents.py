import joblib
import pandas as pd

forecast_model = joblib.load("models/incident_forecast.pkl")

def forecast_incidents():
    return forecast_model[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12).to_dict(orient="records")
