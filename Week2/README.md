# Student Performance Predictor

## Overview
This project, "Student Performance Predictor," is a Week 2 assignment for a machine learning course focused on supervised learning and binary classification. The goal is to predict whether a student will pass or fail based on features from the Student Performance Dataset. The project implements Logistic Regression and Decision Tree models, evaluates them using accuracy, precision, and confusion matrices, and analyzes feature impacts to understand which factors influence student performance. Key tasks include:

- Data preprocessing (encoding categorical variables, creating a Pass/Fail target)
- Training and evaluating Logistic Regression and Decision Tree models
- Visualizing model performance (confusion matrices, feature importance)
- Presenting insights on feature impacts (e.g., test preparation, lunch type)

## Dataset
The dataset used is the [UCI Student Performance Dataset](https://archive.ics.uci.edu/ml/datasets/Student+Performance) or a similar dataset with the following columns:

- **Categorical Features**:
  - `gender`: Student gender (e.g., male, female)
  - `race/ethnicity`: Student race/ethnicity (e.g., group A, group B)
  - `parental level of education`: Parent’s education level (e.g., bachelor's degree, high school)
  - `lunch`: Lunch type (e.g., standard, free/reduced)
  - `test preparation course`: Whether the student completed a test prep course (e.g., completed, none)
- **Numerical Features**:
  - `math score`: Student’s math score
  - `reading score`: Student’s reading score
  - `writing score`: Student’s writing score
- **Derived Target**:
  - `Pass/Fail`: Binary label (Pass=1 if average score ≥ 60, Fail=0 otherwise)

**Source**: Download the dataset from the UCI Machine Learning Repository or use a similar CSV file with the specified columns.

## Prerequisites
To run the analysis script, ensure you have the following installed:

- Python 3.6+
- Required Python libraries:
  ```bash
  pip install pandas scikit-learn matplotlib seaborn
  ```
- The Student Performance Dataset CSV file (named `student-data.csv`).

## Installation
1. **Download the Dataset**:
   - Obtain the UCI Student Performance Dataset from the provided link.
   - Save the CSV file as `student-data.csv` in the project directory.

2. **Set Up the Environment**:
   - Install Python if not already installed (download from [python.org](https://www.python.org)).
   - Install the required libraries by running:
     ```bash
     pip install pandas scikit-learn matplotlib seaborn
     ```

3. **Download the Analysis Script**:
   - Save the provided `student_performance_predictor.py` script in the project directory.

## Usage
The `student_performance_predictor.py` script performs the entire analysis pipeline, including data preprocessing, model training, evaluation, and feature analysis. Follow these steps to use it:

1. **Prepare the Dataset**:
   - Ensure `student-data.csv` is in the project directory alongside `student_performance_predictor.py`.
   - If the dataset has a different name or location, update the `pd.read_csv` line in the script to point to the correct file path (e.g., `pd.read_csv('path/to/student-data.csv')`).

2. **Run the Script**:
   - Open a terminal or command prompt and navigate to the project directory.
   - Run the script using:
     ```bash
     python student_performance_predictor.py
     ```

3. **Outputs**:
   - **Console Output**: The script displays:
     - Dataset shapes (training and testing sets)
     - Model performance metrics (accuracy, precision)
     - Logistic Regression coefficients and Decision Tree feature importance tables
   - **Visualizations**: The following PNG files are generated in the project directory:
     - `log_reg_confusion_matrix.png`: Confusion matrix for Logistic Regression
     - `dec_tree_confusion_matrix.png`: Confusion matrix for Decision Tree
     - `feature_importance.png`: Bar chart of Decision Tree feature importance
   - **Interpreting Results**:
     - Review the console output for model performance and feature analysis.
     - Check the generated PNG files for visualizations supporting the insights.

## Project Structure
```
Week2/
├── student_performance_predictor.py  # Main Python script for analysis
├── student-data.csv                 # Input dataset
```

## Learning Outcomes
This project addresses the following learning objectives:
- **Supervised Learning**: Training models on labeled data to predict Pass/Fail outcomes.
- **Binary Classification**: Building and evaluating models for a binary classification task.
- **Model Evaluation**: Using accuracy, precision, and confusion matrices to compare model performance.
- **Feature Impact Analysis**: Interpreting Logistic Regression coefficients and Decision Tree feature importance to understand key predictors.

## Troubleshooting
- **FileNotFoundError**: Ensure `student-data.csv` is in the project directory or update the file path in the script.
- **Missing Dependencies**: Verify that `pandas`, `scikit-learn`, `matplotlib`, and `seaborn` are installed using `pip install`.
- **Column Mismatches**: If the dataset columns differ (e.g., `sex` instead of `gender`), update the column names in the script to match the dataset.
- **Visualization Issues**: Ensure `matplotlib` and `seaborn` are installed. If visualizations fail to display, try running in an environment like Jupyter Notebook or check for permission issues when saving PNG files.

## Contact
For questions, issues, or feedback about this project, please contact:

- **Email**: muhammadusman.becsef22@iba-suk.edu.pk
- **GitHub**: [https://www.github.com/Usmansarwar143](https://www.github.com/Usmansarwar143)
- **LinkedIn**: [https://www.linkedin.com/in/muhammad-usman-018535253](https://www.linkedin.com/in/muhammad-usman-018535253)

If you need assistance with the script, dataset, or additional visualizations, feel free to reach out!

## License
This project is for educational purposes and uses the UCI Student Performance Dataset, which is publicly available. Ensure you comply with the dataset’s terms of use.
