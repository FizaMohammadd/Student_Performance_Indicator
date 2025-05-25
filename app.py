import streamlit as st
import pickle
import numpy as np

# Load the trained model
model_path = "model.pkl"  # Ensure your trained model is saved as 'model.pkl'
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Student Performance Predictor")
st.write("Enter student details to predict performance")

# Input fields (modify based on your dataset features)
feature1 = st.number_input("Feature 1 (e.g., Study Hours)", min_value=0.0, max_value=24.0, step=0.1)
feature2 = st.number_input("Feature 2 (e.g., Attendance %)", min_value=0, max_value=100, step=1)
feature3 = st.selectbox("Feature 3 (e.g., Extra Curricular Activities)", ["Yes", "No"])

# Convert categorical data
feature3 = 1 if feature3 == "Yes" else 0

# Prediction button
if st.button("Predict Performance"):
    input_data = np.array([[feature1, feature2, feature3]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Score: {prediction[0]:.2f}")

# Run the app with `streamlit run filename.py`