#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000" 
#API_URL = "http://15.206.212.35:8000"


 # Change this to your deployed IP if on EC2

st.set_page_config(page_title="ABC Tech ITSM ML", layout="centered")
st.title("🚀 ITSM ML Dashboard - ABC Tech")

# --- Shared form for ticket data ---
with st.form("ticket_form"):
    st.subheader("🎫 Ticket Input")
    Impact = st.slider("Impact", 1, 5, 3)
    Urgency = st.slider("Urgency", 1, 5, 3)
    Handle_Time_hrs = st.number_input("Handle Time (hrs)", min_value=0.0)
    Resolution_Time_hrs = st.number_input("Resolution Time (hrs)", min_value=0.0)
    No_of_Reassignments = st.number_input("Reassignments", min_value=0.0)
    No_of_Related_Interactions = st.number_input("Related Interactions", min_value=0.0)
    No_of_Related_Incidents = st.number_input("Related Incidents", min_value=0.0)
    No_of_Related_Changes = st.number_input("Related Changes", min_value=0.0)
    Is_Reopened = st.selectbox("Is Reopened?", [0, 1])

    submitted = st.form_submit_button("Submit Ticket")

payload = {
    "Impact": Impact,
    "Urgency": Urgency,
    "Handle_Time_hrs": Handle_Time_hrs,
    "Resolution_Time_hrs": Resolution_Time_hrs,
    "No_of_Reassignments": No_of_Reassignments,
    "No_of_Related_Interactions": No_of_Related_Interactions,
    "No_of_Related_Incidents": No_of_Related_Incidents,
    "No_of_Related_Changes": No_of_Related_Changes,
    "Is_Reopened": Is_Reopened
}

# --- Run ML endpoints on submit ---
if submitted:
    with st.spinner("Sending to ML backend..."):
        high_priority = requests.post(f"http://localhost:8000/predict_priority", json=payload).json()

        #high_priority = requests.post(f"{API_URL}/predict_priority", json=payload).json()
        auto_tag = requests.post(f"{API_URL}/auto_tag_priority", json=payload).json()
        rfc = requests.post(f"{API_URL}/predict_rfc_failure", json=payload).json()

    st.success(f"🔍 High Priority: {'Yes' if high_priority['Is_High_Priority'] else 'No'}")
    st.info(f"🏷️ Predicted Priority: {auto_tag['Predicted_Priority']}")
    st.warning(f"⚠️ RFC Failure Risk: {'High' if rfc['RFC_Failure_Predicted'] else 'Low'}")

# --- Forecasting ---
st.subheader("📊 Forecast Ticket Volume")
if st.button("Get Next 12 Months Forecast"):
    forecast = requests.get(f"{API_URL}/forecast_incidents").json()
    df = pd.DataFrame(forecast)
    st.line_chart(df.set_index("ds")["yhat"])

