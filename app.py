import requests
import streamlit as st

st.title("Premier League points Predictor")

st.write("Enter team statistics")


W = st.number_input("Wins (W)", min_value=0)
D = st.number_input("Draws (D)", min_value=0)
L = st.number_input("Losses (L)", min_value=0)
GF = st.number_input("Goals For (GF)", min_value=0)
GA = st.number_input("Goals Against (GA)", min_value=0)
GD = GF - GA  

st.write(f"Goal Difference (GD): **{GD}**")

if st.button("Predict Points"):
    payload = {
        "W": W,
        "D": D,
        "L": L,
        "GF": GF,
        "GA": GA,
        "GD": GD
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    if response.status_code == 200:
        st.success(
            f"Predicted Points: **{response.json()['predicted_points']:.2f}**"
        )
    else:
        st.error("API error")