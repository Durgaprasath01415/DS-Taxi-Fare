import streamlit as st
import pickle

    
st.title("🚖Taxi Fare Prediction App")

# Input form
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)
trip_distance = st.number_input("Trip Distance (km)", min_value=0.5, step=0.1)
trip_duration = st.number_input("Trip Duration (minutes)", min_value=1.0, step=0.1)
is_night = st.radio("Is it Night?", ['Yes', 'No'])

# Ratecode options (one-hot encoded)
ratecode = st.selectbox("Rate Code", ['1-Standard', '2-JFK', '3-Newark', '4-Nassau', '5-Negotiated', '6-Group Ride'])
ratecode_onehot = [0]*5
if ratecode != '1-Standard':
    ratecode_onehot[int(ratecode[0])-2] = 1

# Payment type (one-hot encoded)
payment = st.selectbox("Payment Type", ['1-Credit Card', '2-Cash', '3-No Charge', '4-Dispute'])
payment_onehot = [0]*3
if payment != '1-Credit Card':
    payment_onehot[int(payment[0])-2] = 1

# Final feature array
features = [[
    passenger_count,
    trip_distance,
    1 if is_night == "Yes" else 0,
    trip_duration,
    *ratecode_onehot,
    *payment_onehot,
]]

# Load your trained model
with open("gb_model.pkl", "rb") as f:
    model = pickle.load(f)
    
# Predict
if st.button("Predict Fare"):
    prediction = model.predict(features)[0]
    st.success(f"💰 Estimated Fare: ${round(prediction, 2)}")
