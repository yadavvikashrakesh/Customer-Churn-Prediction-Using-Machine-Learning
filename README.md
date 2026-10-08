
# Customer Churn Prediction Using Machine Learning

An end-to-end beginner-level AI/ML project that predicts whether a customer is likely to churn.

## Project Overview

Customer churn prediction is a binary classification problem. This project uses customer demographic, subscription, payment, usage, support, and satisfaction information to predict the `churn` target.

### Dataset

- File: `data/customer_churn_15000.csv`
- Rows: 15,100 before duplicate removal
- Columns: 17
- Target: `churn`
- `0` = No churn
- `1` = Churn
- `customer_id` is excluded from model training because it is an identifier.

## Features

### Numerical
- age
- tenure_months
- monthly_charges
- total_charges
- support_calls
- complaints
- late_payments
- satisfaction_score
- is_active

### Categorical
- gender
- city
- state
- contract_type
- payment_method
- internet_service

## Workflow

1. Dataset collection
2. Data cleaning
3. Exploratory Data Analysis
4. Data preprocessing
5. Feature preparation
6. Train/test split
7. Logistic Regression
8. Random Forest
9. Model evaluation
10. Model comparison
11. Model saving
12. Streamlit prediction system

## Models

### Logistic Regression
Accuracy: 0.9303  
Precision: 0.7565  
Recall: 0.8631  
F1-Score: 0.8063  
ROC-AUC: 0.9454

### Random Forest
Accuracy: 0.9340  
Precision: 0.8097  
Recall: 0.7937  
F1-Score: 0.8016  
ROC-AUC: 0.9379

## Final Model

**Selected model: Logistic Regression**

The selection is based primarily on F1-Score because the dataset is imbalanced and churn detection requires a balance between precision and recall.

## Run Locally

### 1. Create environment

```bash
python -m venv venv
```

### 2. Activate

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Streamlit

```bash
streamlit run app.py
```

## Project Structure

```text
Customer-Churn-Prediction/
├── app.py
├── requirements.txt
├── README.md
├── model_comparison.csv
├── data/
│   └── customer_churn_15000-3.csv
├── models/
│   ├── customer_churn_logistic_regression.pkl
│   ├── customer_churn_random_forest.pkl
│   └── customer_churn_best_model.pkl
├── notebooks/
│   └── Customer_Churn_Week4_Final.ipynb
└── reports/
    ├── Project_Report.md
    └── Project_Report.pdf
```

## Future Improvements

- Hyperparameter tuning
- Cross-validation
- Threshold optimization
- SHAP-based explainability
- More customer history
- Real-time API/database integration
- Cloud deployment

## Disclaimer

The prediction is a machine learning estimate and should be used as decision support rather than a guaranteed outcome.
>>>>>>> 5517f99 (Customer_prediction)
