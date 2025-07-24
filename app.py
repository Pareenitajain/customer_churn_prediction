import streamlit as st
import joblib
import pandas as pd

# Load model and feature list
model = joblib.load("decision_tree_model.pkl")
features = joblib.load("model_features.pkl")

st.set_page_config(page_title="Customer Churn Predictor", layout="wide")
st.title("📉 Customer Churn Prediction App")

# Test display to confirm app loaded
st.write("✅ App loaded successfully!")

# Input fields
st.subheader("Enter Customer Details:")

input_data = {}
for feature in features:
    input_data[feature] = st.number_input(f"{feature}", step=1.0)

# Predict button
if st.button("Predict Churn"):
    input_df = pd.DataFrame([input_data], columns=features)
    prediction = model.predict(input_df)
    st.success(f"🔍 Prediction: {'Churn' if prediction[0] == 1 else 'No Churn'}")
