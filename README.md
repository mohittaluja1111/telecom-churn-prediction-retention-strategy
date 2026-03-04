# Telecom Churn Prediction & Retention Intelligence System

## Project Summary

Customer churn directly impacts revenue in the telecom industry. This project delivers a complete data-driven solution to identify customers at risk of churn and recommend targeted retention actions.

## It combines:

📊 Exploratory Data Analysis (EDA)

🧠 Machine Learning (XGBoost Pipeline)

⚙️ Feature Engineering

🌐 Interactive Streamlit Dashboard

➡️ The goal is to shift from reactive churn handling → proactive retention strategy

## Business Objective

The primary objective is to:

Predict churn probability for each customer

Understand key behavioral and financial drivers

Enable telecom teams to take timely retention actions

## Data Overview

The dataset includes multiple dimensions of customer behavior:

Customer Lifecycle → tenure, contract type

Financial Data → monthly charges, payment behavior

Customer Experience → complaints, service usage

Engagement Metrics → app usage, transactions

## Target Variable

is_churn → Indicates whether a customer has churned

## Feature Engineering (Key Highlight)

To enhance model performance, new business-driven features were created:

engagement_score → Customer activity level

payment_risk → Likelihood of delayed payments

clv_proxy → Estimated customer lifetime value

These features helped capture real-world customer behavior patterns beyond raw data.

## Exploratory Data Analysis

EDA revealed strong churn patterns:

📉 Customers with low tenure are more likely to churn

💸 Higher monthly charges increase churn probability

📑 Month-to-month contracts show higher churn risk

⚠️ Frequent complaints strongly correlate with churn

## Visual analysis included:

Distribution plots

Churn segmentation charts

Correlation heatmaps

<img width="716" height="622" alt="EDA-1" src="https://github.com/user-attachments/assets/3066b32e-7b66-433b-b93a-365cea7f5ea1" />
<img width="1042" height="563" alt="EDA-2" src="https://github.com/user-attachments/assets/94c05885-39f2-4f07-9f09-3404beca8dd8" />
<img width="816" height="603" alt="EDA-3" src="https://github.com/user-attachments/assets/d64e5d53-6de9-463f-87c1-405fe18e1a36" />
<img width="448" height="590" alt="EDA-4" src="https://github.com/user-attachments/assets/9c17b714-119f-40bd-b83e-8ad9b0a42006" />
<img width="701" height="427" alt="EDA-5" src="https://github.com/user-attachments/assets/00a81b23-8139-4071-a753-af00cfc2b5f3" />

## Modeling Approach

A machine learning pipeline was built to ensure consistency and scalability:

## Preprocessing

Standardization of numerical features

One-hot encoding for categorical variables

## Model

XGBoost Classifier (optimized for tabular data)

## Pipeline Advantage

Eliminates preprocessing mismatch

Ensures seamless deployment in Streamlit

# Model Evaluation

The model was evaluated using:

## ROC-AUC Score

Precision & Recall

F1-Score

<img width="868" height="492" alt="ROC-AUC Score" src="https://github.com/user-attachments/assets/abc94921-fec4-4346-814e-d7fea47efea8" />

## Confusion Matrix

✔️ Strong performance in identifying high-risk churn customers
✔️ Focus on recall to minimize missed churn cases

<img width="720" height="687" alt="Confusion Matrix" src="https://github.com/user-attachments/assets/5a1117de-42fb-41a8-b261-ae3cf0db527a" />

## Key Insights

New customers are highly prone to churn

Flexible contracts increase churn likelihood

Low engagement is a major churn signal

Payment delays indicate financial risk behavior

💼 Business Recommendations

🎯 Target high-risk customers with personalized offers

📶 Improve service quality and complaint handling

📱 Increase engagement through app-based incentives

💳 Encourage auto-pay to reduce payment-related churn

🤖 Integrate model into CRM for proactive retention

## Streamlit Application

An interactive web application was developed to make the model usable for business teams.

✨ Features

Real-time churn prediction

User-friendly input interface

Risk categorization (High / Medium / Low)

Actionable business recommendations

Visual indicators (metrics + progress bar)

<img width="1903" height="995" alt="Snip 1" src="https://github.com/user-attachments/assets/f6077bde-c65d-47ec-8ede-37bd8dce06db" />
<img width="1908" height="1010" alt="Snip 2" src="https://github.com/user-attachments/assets/86623bd8-1a02-49b4-af35-8759a4963095" />
<img width="1905" height="1010" alt="Snip 3" src="https://github.com/user-attachments/assets/70ddbfdb-b088-43c7-86f2-28b088d52881" />
<img width="1906" height="1012" alt="Snip 4" src="https://github.com/user-attachments/assets/73408dab-0646-40da-aa24-1b91ef9eedc1" />


## Running the Project

1️⃣ Clone Repository

git clone <your-repo-link>

cd telecom-churn-prediction-retention-strategy

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Streamlit App

cd app

streamlit run app.py

## Repository Structure

telecom-churn-prediction-retention-strategy/

### data/

 ── telecom_churn.csv
 
 ── data_definition.xlsx

### notebooks/

 ── churn_analysis.ipynb

### app/

 ── app.py
 
 ── model.pkl
 
 ── requirements.txt

### images/

 ── dashboard.png
 

 ── README.md
 
 ── .gitignore

## Conclusion

This project demonstrates how machine learning can be effectively used to predict customer churn and drive business decisions.

By combining predictive modeling with actionable insights and an interactive dashboard, the solution enables telecom companies to:

Reduce churn rate

Optimize retention strategies

Improve customer lifetime value

## Author

Mohit Taluja
Aspiring Data Scientist | AI & Analytics Enthusiast

## Support

If this project adds value:
👉 Star the repository
👉 Share your feedback
