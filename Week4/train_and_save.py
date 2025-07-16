import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def load_and_preprocess_data(train_file, test_file):
    # Load training and testing datasets
    train_data = pd.read_csv(train_file)
    test_data = pd.read_csv(test_file)
    
    # Verify expected columns
    expected_columns = ['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 
                       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 
                       'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    if not all(col in train_data.columns for col in expected_columns + ['Loan_Status']):
        raise ValueError("Training data missing expected columns")
    if not all(col in test_data.columns for col in expected_columns):
        raise ValueError("Test data missing expected columns")
    
    # Handle missing values for both datasets
    for data in [train_data, test_data]:
        data['LoanAmount'] = data['LoanAmount'].fillna(data['LoanAmount'].mean())
        data['Loan_Amount_Term'] = data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0])
        data['Credit_History'] = data['Credit_History'].fillna(data['Credit_History'].mode()[0])
        data['Gender'] = data['Gender'].fillna(data['Gender'].mode()[0])
        data['Married'] = data['Married'].fillna(data['Married'].mode()[0])
        data['Dependents'] = data['Dependents'].fillna(data['Dependents'].mode()[0])
        data['Self_Employed'] = data['Self_Employed'].fillna(data['Self_Employed'].mode()[0])
    
    # Encode categorical variables
    le = LabelEncoder()
    categorical_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
    for col in categorical_cols:
        # Fit on training data and transform both datasets
        train_data[col] = le.fit_transform(train_data[col])
        test_data[col] = le.transform(test_data[col])
    
    # Save label encoder for target
    target_le = LabelEncoder()
    train_data['Loan_Status'] = target_le.fit_transform(train_data['Loan_Status'])
    
    # Features and target for training
    X_train = train_data.drop(['Loan_ID', 'Loan_Status'], axis=1)
    y_train = train_data['Loan_Status']
    
    # Features for testing
    X_test = test_data.drop(['Loan_ID'], axis=1)
    
    # Scale numerical features
    scaler = StandardScaler()
    numerical_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']
    # Fit scaler on training data and transform both
    X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
    X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])
    
    # Save scaler and feature names
    joblib.dump(scaler, 'scaler.joblib')
    joblib.dump(X_train.columns, 'feature_names.joblib')
    
    # Check if test data has Loan_Status for evaluation
    y_test = None
    if 'Loan_Status' in test_data.columns:
        y_test = target_le.transform(test_data['Loan_Status'])
    
    return X_train, y_train, X_test, y_test

def train_model(train_file='train_u6lujuX_CVtuZ9i.csv', test_file='test_Y3wMUE5_7gLdaTN.csv'):
    X_train, y_train, X_test, y_test = load_and_preprocess_data(train_file, test_file)
    
    # Train RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate model on test set if y_test exists
    if y_test is not None:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        print(f"Model Accuracy on Test Set: {accuracy:.2f}")
        print("Classification Report:")
        print(report)
    else:
        print("Test set does not contain Loan_Status. Skipping evaluation.")
    
    # Save model
    joblib.dump(model, 'loan_prediction_model.joblib')
    print("Model, scaler, and feature names saved successfully.")

if __name__ == "__main__":
    train_model()