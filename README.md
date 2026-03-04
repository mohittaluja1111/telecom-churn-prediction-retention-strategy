# 📡 Churn Prediction & Retention Strategy for a Telecom Provider

### 👤 Author: Mohit Taluja  
### 🎓 Capstone Project | Data Science | Machine Learning  

---

## 🚀 Project Overview
Customer churn is a major challenge in the telecom industry, directly impacting revenue and growth.  
This project builds an **end-to-end Machine Learning pipeline** to predict customer churn and provide actionable retention strategies.

---

## 🎯 Problem Statement
- High customer churn leads to revenue loss  
- Retaining customers is cheaper than acquiring new ones  
- Goal: **Predict churn + enable proactive retention**

---

## 📊 Dataset Overview
The dataset includes:

- 👤 Customer demographics  
- 📶 Service usage patterns  
- 💳 Billing & payment details  
- 📉 Complaint & engagement metrics  

**Target Variable:**  
`is_churn (1 = churn, 0 = retained)`

---

## 🔍 Exploratory Data Analysis (EDA)

### 📌 Key Insights:
- Low tenure customers are more likely to churn  
- High monthly charges increase churn risk  
- Complaints strongly correlate with churn  

### 📷 Visualizations:
 <img width="716" height="622" alt="EDA-1" src="https://github.com/user-attachments/assets/13d488ef-4d52-4dda-b55e-9ee91a0897fa" />
<img width="1042" height="563" alt="EDA-2" src="https://github.com/user-attachments/assets/213573fb-ed9b-4a8d-9097-1c44bcdfbd16" />
<img width="816" height="603" alt="EDA-3" src="https://github.com/user-attachments/assets/7239df9a-1d08-4399-a89c-36ccd6789bef" />
<img width="448" height="590" alt="EDA-4" src="https://github.com/user-attachments/assets/80f0773b-85a4-4adc-8148-e6a87a57079a" />
<img width="701" height="427" alt="EDA-5" src="https://github.com/user-attachments/assets/e4cf2100-ee7d-4f4a-931b-c9841ffccb1b" />

---

## ⚙️ Feature Engineering

Created powerful features to improve model performance:

- 📊 **Engagement Score** → app activity + transactions  
- ⚠️ **Payment Risk** → delays + late payments  
- 💰 **CLV Proxy** → revenue × tenure  

---

## 🤖 Model Building

Models used:
- Logistic Regression  
- Random Forest  
- ⭐ XGBoost (Final Model)  

### 🔧 Pipeline:
- Data preprocessing  
- Scaling & encoding  
- Model training  

---

## 📈 Model Evaluation

### 📊 Performance Metrics:
- ROC-AUC Score: **0.60+**  
- Precision, Recall, F1-score  

### 📷 Visuals:
<img width="720" height="687" alt="Confusion Matrix" src="https://github.com/user-attachments/assets/9b644302-f0fd-4ea8-a47c-98f7841e9ee7" />
<img width="868" height="492" alt="ROC-AUC Score" src="https://github.com/user-attachments/assets/de09e3b5-6cda-4250-bc4d-3c1cc3d2877e" />

---

## 💡 Key Business Insights

- 📉 Low tenure → high churn risk  
- 💸 High charges → dissatisfaction  
- 📞 Frequent complaints → churn signal  

---

## 🧠 Business Recommendations

- 🎯 Target high-risk customers  
- 💰 Offer personalized discounts  
- ⚡ Improve service quality  
- 📲 Increase customer engagement  

---

## 🖥️ Streamlit Web App

An interactive dashboard to:
- Input customer details  
- Predict churn probability  
- Get risk level & recommendations  

### 📷 App Screens:
 <img width="1903" height="995" alt="Snip 1" src="https://github.com/user-attachments/assets/5ba49c8d-1298-46b4-a9c4-19e59fedc070" />
<img width="1908" height="1010" alt="Snip 2" src="https://github.com/user-attachments/assets/7e8c687e-9069-499b-aca0-2861c18ea0b0" />
<img width="1905" height="1010" alt="Snip 3" src="https://github.com/user-attachments/assets/489251a2-0d58-4374-81a7-0a68287f3b38" />
<img width="1906" height="1012" alt="Snip 4" src="https://github.com/user-attachments/assets/1265d04e-1915-45aa-976f-34778edab9a8" />

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Streamlit  
- Matplotlib, Seaborn  

---

## 📂 Project Structure

Telecom-Churn/
│
├── data/
├── notebook/
├── app/
├── model/
├── images/
├── requirements.txt
└── README.md

---

## 🚀 How to Run

```bash
git clone <your-repo-link>
cd Telecom-Churn
pip install -r requirements.txt
streamlit run app.py

🏁 Conclusion

This project demonstrates how Machine Learning can drive business decisions by predicting churn and enabling proactive retention strategies, ultimately improving customer lifetime value.

⭐ Connect with Me

🔗 LinkedIn: (www.linkedin.com/in/mohit-taluja)
📂 GitHub: (your profile link)

⭐ If you found this project useful, give it a star!
