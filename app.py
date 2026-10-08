import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder



st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction")
st.write("Enter customer details to predict whether the customer is likely to churn.")



model = joblib.load("models/Customer_churn_best_model.pkl")


preprocessor = model.named_steps["preprocessor"]

cat_pipeline = preprocessor.named_transformers_["cat"]

encoder = cat_pipeline.named_steps["encoder"]

categorical_columns = [
    "gender",
    "city",
    "state",
    "contract_type",
    "payment_method",
    "internet_service"
]

category_options = {}

for column, categories in zip(
    categorical_columns,
    encoder.categories_
):
    category_options[column] = list(categories)



st.subheader("👤 Customer Information")



age = st.number_input(
    "Age",
    min_value=0,
    max_value=100,
    value=30
)

tenure_months = st.number_input(
    "Tenure Months",
    min_value=0,
    value=12
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=500.0,
    step=10.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=5000.0,
    step=100.0
)

support_calls = st.number_input(
    "Support Calls",
    min_value=0,
    value=1
)

complaints = st.number_input(
    "Complaints",
    min_value=0,
    value=0
)

late_payments = st.number_input(
    "Late Payments",
    min_value=0,
    value=0
)

satisfaction_score = st.number_input(
    "Satisfaction Score",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)


st.subheader("📋 Customer Details")

is_active = st.selectbox(
    "Is Active",
    [0, 1],
    format_func=lambda x: "Active" if x == 1 else "Inactive"
)

gender = st.selectbox(
    "Gender",
    category_options["gender"]
)


city = st.selectbox(
    "City",
    category_options["city"]
)

state = st.selectbox(
    "State",
    category_options["state"]
)

contract_type = st.selectbox(
    "Contract Type",
    category_options["contract_type"]
)
payment_method = st.selectbox(
    "Payment Method",
    category_options["payment_method"]
)

internet_service = st.selectbox(
    "Internet Service",
    category_options["internet_service"]
)



input_data = pd.DataFrame({
    "age": [age],
    "gender": [gender],
    "city": [city],
    "state": [state],
    "tenure_months": [tenure_months],
    "contract_type": [contract_type],
    "payment_method": [payment_method],
    "monthly_charges": [monthly_charges],
    "total_charges": [total_charges],
    "internet_service": [internet_service],
    "support_calls": [support_calls],
    "complaints": [complaints],
    "late_payments": [late_payments],
    "satisfaction_score": [satisfaction_score],
    "is_active": [is_active]
})



st.divider()

if st.button("🔮 Predict Churn", use_container_width=True):

    prediction = model.predict(input_data)

    st.subheader("Prediction")

    if prediction[0] == 1:

        st.error(
            "⚠️ Customer is likely to Churn"
        )

    else:

        st.success(
            "✅ Customer is likely to Stay"
        )



with st.expander("🔍 View Input Data"):

    st.dataframe(
        input_data,
        use_container_width=True
    )