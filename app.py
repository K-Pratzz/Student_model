import streamlit as st
import numpy as np
import joblib 
model=joblib.load("Student_model.pkl") 
st.title("Student Score Predictor")

# Inputs from user
st.header("HOURS OF STUDY")
feature1 = st.number_input("Enter Study Time:", min_value=0.0,max_value=20.0)
st.header("Hours of travel")
feature2 = st.number_input("Enter Travel time:", min_value=0.0,max_value=20.0)
st.write("wait..................")
# Predict button
if st.button("Predict"):
    input_data = np.array([[feature1, feature2]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Score: {prediction}")