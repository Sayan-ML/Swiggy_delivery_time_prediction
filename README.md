# 📦 Delivery Time Prediction System
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)  
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-yellow.svg)  
![LightGBM](https://img.shields.io/badge/LightGBM-Gradient--Boosting-brightgreen.svg)  
![XGBoost](https://img.shields.io/badge/XGBoost-Ensemble-orange.svg)  
![Optuna](https://img.shields.io/badge/Optuna-Hyperparameter%20Tuning-purple.svg)  
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)  

---

## 📖 Description  
This project focuses on building a **high-performing regression system** to predict **delivery times** from a dataset of **40,000 entries (Kaggle)**.  

- Conducted **data preprocessing, EDA, feature engineering, feature selection**  
- Trained multiple **regression models** and compared their performance  
- Leveraged **ensemble techniques** to boost accuracy  
- Final model: **Voting Regressor (XGBoost + LightGBM)**  
- Achieved **R² score = 0.88**, ensuring reliable delivery time predictions  

🔗 **Live Demo:** [Google Drive Link](https://drive.google.com/file/d/1D-7lHpS17M5VTUDwQ3lMRXEPs0AdKkSN/view?usp=sharing)  

---

## 📊 Dataset Overview  

- **Source:** Kaggle  
- **Size:** 40,000 rows  
- **Features:**  
  - Order Date  
  - Delivery Location  
  - Shipment Mode  
  - Product Type  
  - Other delivery-related attributes  

---

## 🧹 Data Preprocessing  

- **Missing Value Handling:**  
  - Iterative Imputer, KNN Imputer, and distribution-based imputation were tested  
  - Dropping missing values yielded the best baseline performance  

- **Other Steps:**  
  - Standardization for numerical features  
  - Encoding categorical features  
  - Outlier detection and removal  

---

## 🔍 Exploratory Data Analysis (EDA)  

- Distribution plots to understand feature skewness  
- Correlation heatmaps for feature interactions  
- Pairwise plotting for visualizing dependencies  
- Outlier detection (delivery delays, anomalies)  

---

## 🧠 Feature Selection  

- Tested: **Forward Selection, RFE, Variance Inflation Factor (VIF)**  
- Decision: Retained **all features**, as they contributed positively to accuracy  

---

## 🤖 Model Training & Optimization  

Models Trained:  
- **XGBoost**  
- **LightGBM**  
- **Random Forest Regressor**  
- **Support Vector Regressor (SVR)**  
- **Linear Regression**
- **Feed Forward Neural Network**

Optimization:  
- Hyperparameter tuning with **Optuna (Bayesian Optimization)**  
- Final Model: **Voting Regressor (XGBoost + LightGBM)**  
- **R² Score = 0.88**  

---

## 🌟 Future Improvements  

- Integrate **Deep Learning regression models** (e.g., TabNet, Transformers for tabular data)  
- Build a **Streamlit dashboard** for interactive prediction  
- Add **explainable AI (XAI)** using SHAP or LIME  
- Deploy with **Docker/Kubernetes** for scalability  
- Expand dataset with **real-time logistics data**  

---

## 🤝 Contributing  

We welcome contributions!  
1. Fork the repository 🍴  
2. Create your feature branch 🌱 (`git checkout -b feature-xyz`)  
3. Commit your changes ✔️ (`git commit -m "Added feature XYZ"`)  
4. Push to the branch 🚀 (`git push origin feature-xyz`)  
5. Open a Pull Request 🔥  

---

## 💖 Show Your Support  

If you like this project, **please ⭐ the repo** and share with others 🙌  

---

## 📜 License  

This project is licensed under the **MIT License** – free to use, modify, and distribute with attribution.  

---

## 👨‍💻 Developed By  

**Sayan Banerjee**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/sayan-banerjee-0222a4214/) 
[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/Sayan-ML) 
