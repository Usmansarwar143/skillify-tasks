import streamlit as st
import pandas as pd
import joblib

# Load saved model, scaler, and feature names
model = joblib.load('loan_prediction_model.joblib')
scaler = joblib.load('scaler.joblib')
feature_names = joblib.load('feature_names.joblib')

# Streamlit interface
def main():
    # Set page config for better appearance
    st.set_page_config(page_title="Loan Approval Prediction", page_icon="💰", layout="centered")
    
    # Custom CSS for styling
    st.markdown("""
    <style>
    .main {background-color: #f0f2f6;}
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stNumberInput, .stSelectbox {
        background-color: black;
        border-radius: 5px;
        padding: 5px;
    }
    .header {
        color: #2c3e50;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subheader {
        color: #34495e;
        font-size: 20px;
        margin-top: 20px;
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .approved {background-color: #d4edda; color: #155724;}
    .not-approved {background-color: #f8d7da; color: #721c24;}
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="header">Loan Approval Prediction System</div>', unsafe_allow_html=True)
    st.write("Enter the details below to predict loan approval status")
    
    # Input form with two columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
    
    with col2:
        applicant_income = st.number_input("Applicant Income", min_value=0.0, step=100.0)
        coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, step=100.0)
        loan_amount = st.number_input("Loan Amount", min_value=0.0, step=1000.0)
        loan_amount_term = st.number_input("Loan Amount Term (months)", min_value=0.0, step=12.0)
        credit_history = st.selectbox("Credit History (1=Good, 0=Bad)", [1.0, 0.0])
    
    if st.button("Predict Loan Status", key="predict"):
        # Prepare input data
        input_data = pd.DataFrame({
            'Gender': [1 if gender == "Male" else 0],
            'Married': [1 if married == "Yes" else 0],
            'Dependents': [3 if dependents == "3+" else int(dependents)],
            'Education': [0 if education == "Graduate" else 1],
            'Self_Employed': [1 if self_employed == "Yes" else 0],
            'ApplicantIncome': [applicant_income],
            'CoapplicantIncome': [coapplicant_income],
            'LoanAmount': [loan_amount],
            'Loan_Amount_Term': [loan_amount_term],
            'Credit_History': [credit_history],
            'Property_Area': [{"Urban": 2, "Semiurban": 1, "Rural": 0}[property_area]]
        }, columns=feature_names)
        
        # Scale numerical features
        numerical_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
        input_data[numerical_cols] = scaler.transform(input_data[numerical_cols])
        
        # Make prediction
        prediction = model.predict(input_data)
        result = "Approved" if prediction[0] == 1 else "Not Approved"
        
        # Display result with styling
        result_class = "approved" if result == "Approved" else "not-approved"
        st.markdown(f'<div class="result {result_class}">Loan Status: {result}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()