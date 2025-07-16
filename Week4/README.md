# Loan Approval Prediction System

## Project Overview

This project implements an end-to-end machine learning pipeline for predicting loan approval status based on applicant details. It uses a Random Forest Classifier trained on a loan prediction dataset, with preprocessing steps to handle missing values, encode categorical variables, and scale numerical features. The trained model is saved for reuse and integrated into a user-friendly Streamlit web interface for making predictions on new data.

### Learning Objectives
- Build a complete ML pipeline: data preprocessing, model training, evaluation, and deployment.
- Implement real-world prediction flow with model persistence using `joblib`.
- Create an interactive interface with Streamlit for user input and prediction display.

## Requirements

- **Python**: Version 3.8 or higher
- **Libraries**:
  - `pandas` (>=1.5.0)
  - `numpy` (>=1.21.0)
  - `scikit-learn` (>=1.0.0)
  - `joblib` (>=1.1.0)
  - `streamlit` (>=1.10.0)
- **Dataset**: Two CSV files (`train_loan_data.csv` and `test_loan_data.csv`) with the following columns:
  - **Training Dataset**: `Loan_ID`, `Gender`, `Married`, `Dependents`, `Education`, `Self_Employed`, `ApplicantIncome`, `CoapplicantIncome`, `LoanAmount`, `Loan_Amount_Term`, `Credit_History`, `Property_Area`, `Loan_Status`
  - **Test Dataset**: Same as training, excluding `Loan_Status`

## Installation

1. **Clone the Repository** (if applicable):
   ```bash
   git clone https://github.com/Usmansarwar143/skillify-tasks/Task4
   cd loan-approval-prediction
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended) and install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install pandas numpy scikit-learn joblib streamlit
   ```

3. **Prepare the Dataset**:
   - Download the dataset (e.g., from [Kaggle's Loan Prediction Problem Dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)).
   - Place `train_loan_data.csv` and `test_loan_data.csv` in the project directory.
   - Ensure the training dataset includes `Loan_Status`, while the test dataset may exclude it.

## Dataset

The project uses two CSV files:
- **`train_loan_data.csv`**: Contains training data with features and the target variable (`Loan_Status`).
- **`test_loan_data.csv`**: Contains test data for evaluation or predictions, typically without `Loan_Status`.

### Column Descriptions
| Column             | Description                                      |
|--------------------|--------------------------------------------------|
| Loan_ID           | Unique identifier for each loan application       |
| Gender            | Applicant gender (Male/Female)                   |
| Married           | Marital status (Yes/No)                         |
| Dependents        | Number of dependents (0, 1, 2, 3+)              |
| Education         | Education level (Graduate/Not Graduate)         |
| Self_Employed     | Self-employment status (Yes/No)                 |
| ApplicantIncome   | Applicant's income                              |
| CoapplicantIncome | Co-applicant's income                           |
| LoanAmount        | Loan amount requested                           |
| Loan_Amount_Term  | Loan repayment term (in months)                 |
| Credit_History    | Credit history status (1=Good, 0=Bad)           |
| Property_Area     | Property location (Urban/Semiurban/Rural)       |
| Loan_Status       | Loan approval status (Y/N, in training data only) |

### Preprocessing
- **Missing Values**: Numerical columns (e.g., `LoanAmount`) are filled with the mean; categorical columns (e.g., `Gender`) are filled with the mode.
- **Encoding**: Categorical variables are encoded using `LabelEncoder`, with encoding fitted on training data and applied to both datasets.
- **Scaling**: Numerical features (`ApplicantIncome`, `CoapplicantIncome`, `LoanAmount`, `Loan_Amount_Term`) are scaled using `StandardScaler`.

## Usage

### 1. Training the Model
Run the training script to preprocess the data, train the Random Forest Classifier, and save the model, scaler, and feature names.

```bash
python train_model.py
```

- **Inputs**: `train_loan_data.csv` and `test_loan_data.csv` in the project directory.
- **Outputs**:
  - `loan_prediction_model.joblib`: Trained Random Forest model.
  - `scaler.joblib`: Fitted `StandardScaler` for numerical features.
  - `feature_names.joblib`: List of feature names for consistent input formatting.
  - Console output: If `Loan_Status` is present in the test set, accuracy and classification report are printed; otherwise, evaluation is skipped.

### 2. Running the Streamlit App
Launch the Streamlit web interface to input new data and predict loan approval status.

```bash
streamlit run app.py
```

- **Interface**:
  - Open the provided URL (e.g., `http://localhost:8501`) in your browser.
  - Enter applicant details in a two-column form (e.g., Gender, Income, Loan Amount).
  - Click "Predict Loan Status" to see the prediction ("Approved" or "Not Approved").
- **Features**:
  - Clean, centered layout with custom styling.
  - Color-coded results (green for Approved, red for Not Approved).
  - Input validation and scaling consistent with training preprocessing.

## File Structure

```
Task4/
├── train_u6lujuX_CVtuZ9i.csv       # Training dataset
├── test_Y3wMUE5_7gLdaTN.csv        # Test dataset
├── train_and_save.py            # Script to preprocess data, train model, and save artifacts
├── main.py                    # Streamlit app for predictions
├── loan_prediction_model.joblib  # Saved model (generated after running train_model.py)
├── scaler.joblib             # Saved scaler (generated after running train_model.py)
├── feature_names.joblib      # Saved feature names (generated after running train_model.py)
├── README.md                 # Project documentation
```

## Notes

- **Dataset Source**: If you don't have the dataset, download it from Kaggle (e.g., [Loan Prediction Problem Dataset](https://www.kaggle.com/datasets/altruist/delhi-house-price-prediction)). Rename the files to `train_loan_data.csv` and `test_loan_data.csv` or update the `train_file` and `test_file` parameters in `train_model.py`.
- **Test Dataset**: The test dataset typically lacks `Loan_Status`, so evaluation is skipped. If your test dataset includes `Loan_Status`, the script will evaluate the model and print metrics.
- **Troubleshooting**:
  - **FileNotFoundError**: Ensure CSV files are in the project directory or provide full paths in `train_model.py`.
  - **Column Errors**: Verify that both datasets have the expected columns (listed above). The script includes column validation to catch mismatches.
  - **Streamlit Issues**: Ensure `loan_prediction_model.joblib`, `scaler.joblib`, and `feature_names.joblib` are present before running `app.py`.
- **Extending the Project**:
  - Try other models (e.g., Logistic Regression, XGBoost) by modifying `train_model.py`.
  - Enhance the Streamlit app with additional visualizations or input validation.
  - Add cross-validation in `train_model.py` for more robust evaluation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details (if included).
