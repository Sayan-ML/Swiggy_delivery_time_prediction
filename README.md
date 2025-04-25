📦 Delivery Time Prediction using Ensemble Regression Models
This project focuses on building a high-performing regression model to predict delivery times based on a rich dataset of 40,000 entries sourced from Kaggle. Through meticulous data preprocessing, exploratory data analysis, feature selection, model training, and ensemble techniques, we achieved an impressive R² score of 0.88 using a Voting Regressor combining XGBoost and LightGBM.

📊 Dataset Overview
Source: Kaggle

Size: 40,000 rows

Features: Includes delivery-related attributes such as order date, delivery location, shipment mode, product type, and more.

🧹 Data Preprocessing
Missing Value Handling:

Tried multiple imputation techniques: Iterative Imputer, KNN Imputer, and distribution-based imputation.

Also evaluated the impact of dropping missing values entirely.

Dropping missing values resulted in the best baseline model performance and was selected for final processing.

Standardization and encoding were applied where necessary to prepare the dataset for model training.

🔍 Exploratory Data Analysis (EDA)
Visualized feature distributions and relationships to uncover key drivers of delivery time.

Identified influential variables and detected outliers and skewed distributions.

Performed correlation analysis and pairwise plotting to understand feature interactions.

🧠 Feature Selection
Evaluated multiple selection techniques:

Forward Feature Selection

Recursive Feature Elimination (RFE)

Variance Inflation Factor (VIF)

After assessing the impact of feature selection on model performance, all features were retained, as they contributed positively to overall accuracy.

🤖 Model Training & Optimization
Trained and compared the following regression models:

XGBoost

LightGBM

Random Forest Regressor

Support Vector Regressor (SVR)

Linear Regression

Hyperparameter tuning was conducted using Optuna, leveraging Bayesian Optimization for efficient search across complex parameter spaces.
