from fastapi import FastAPI
from app.predict_priority import predict_high_priority
from app.forecast_incidents import forecast_incidents
from app.auto_tag import predict_priority_tag
from app.predict_rfc import predict_rfc_failure

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to ABC Tech ITSM ML API"}

@app.post("/predict_priority")
def api_predict_priority(payload: dict):
    return predict_high_priority(payload)

@app.get("/forecast_incidents")
def api_forecast_incidents():
    return forecast_incidents()

@app.post("/auto_tag_priority")
def api_auto_tag(payload: dict):
    return predict_priority_tag(payload)

@app.post("/predict_rfc_failure")
def api_predict_rfc(payload: dict):
    return predict_rfc_failure(payload)
