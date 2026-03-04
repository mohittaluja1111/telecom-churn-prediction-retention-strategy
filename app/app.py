import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Telecom Churn AI",
    page_icon="📡",
    layout="wide"
)

# -------------------------------
# LOAD MODEL
# -------------------------------
model = pickle.load(open('model.pkl', 'rb'))

# -------------------------------
# HEADER
# -------------------------------
st.title("📡 Telecom Churn Prediction Dashboard")
st.markdown("### Predict customer churn risk & get actionable insights")

st.markdown("---")

# -------------------------------
# SIDEBAR INPUT
# -------------------------------
st.sidebar.header("📋 Customer Inputs")

tenure = st.sidebar.slider("Tenure (Months)", 1, 120, 12)
monthly = st.sidebar.number_input("Monthly Charges", 100, 2000, 500)
complaints = st.sidebar.slider("Complaints (Last 3 Months)", 0, 10, 1)
logins = st.sidebar.slider("App Logins", 0, 50, 10)
transactions = st.sidebar.slider("Selfcare Transactions", 0, 50, 5)
delay = st.sidebar.slider("Payment Delay (Days)", 0.0, 15.0, 1.0)
late_flag = st.sidebar.selectbox("Late Payment Flag", [0, 1])
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month","One year","Two year"])
plan = st.sidebar.selectbox("Plan Type", ["Prepaid","Postpaid"])

# -------------------------------
# FEATURE ENGINEERING (SAME AS TRAINING)
# -------------------------------
engagement_score = logins + transactions
payment_risk = delay + late_flag

# -------------------------------
# INPUT DATAFRAME
# -------------------------------
input_df = pd.DataFrame([{
    'tenure_months': tenure,
    'monthly_charges': monthly,
    'num_complaints_3m': complaints,
    'engagement_score': engagement_score,
    'payment_risk': payment_risk,
    'contract_type': contract,
    'plan_type': plan
}])

# -------------------------------
# MAIN LAYOUT
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Customer Profile")
    st.dataframe(input_df)

with col2:
    st.subheader("ℹ️ Key Indicators")
    st.metric("Tenure", f"{tenure} months")
    st.metric("Monthly Charges", f"₹{monthly}")
    st.metric("Engagement Score", engagement_score)

st.markdown("---")

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("🔍 Predict Churn Risk"):

    prob = model.predict_proba(input_df)[0][1]

    st.subheader("📈 Prediction Result")

    # -------------------------------
    # METRICS DISPLAY
    # -------------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Churn Probability", f"{prob:.2f}")

    if prob > 0.7:
        col2.metric("Risk Level", "High 🔴")
    elif prob > 0.4:
        col2.metric("Risk Level", "Medium 🟡")
    else:
        col2.metric("Risk Level", "Low 🟢")

    col3.metric("Retention Priority", "High" if prob > 0.7 else "Moderate")

    # -------------------------------
    # PROGRESS BAR (VISUAL IMPACT)
    # -------------------------------
    st.progress(float(prob))

    st.markdown("---")

    # -------------------------------
    # SMART RECOMMENDATIONS
    # -------------------------------
    st.subheader("💡 Recommended Actions")

    if prob > 0.7:
        st.error("🔴 High Risk Customer")
        st.write("✔ Offer personalized discount")
        st.write("✔ Provide priority support")
        st.write("✔ Suggest long-term contract")

    elif prob > 0.4:
        st.warning("🟡 Medium Risk Customer")
        st.write("✔ Send targeted offers")
        st.write("✔ Improve engagement")
        st.write("✔ Monitor behavior closely")

    else:
        st.success("🟢 Low Risk Customer")
        st.write("✔ Upsell premium plans")
        st.write("✔ Cross-sell services")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("Built with ❤️ | Telecom Churn AI Project")