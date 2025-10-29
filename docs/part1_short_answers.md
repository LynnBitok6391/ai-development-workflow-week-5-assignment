# PART 1 — Short Answer Questions

## 1. Problem Definition

**Hypothetical AI Problem:** Develop an AI system to predict fraudulent credit card transactions in real-time.

**3 Objectives:**
- Reduce fraudulent transactions by 30% within the first year.
- Minimize false positives to avoid blocking legitimate transactions.
- Enhance security measures for financial institutions.

**2 Stakeholders:**
- Financial institutions: To protect against fraud.
- Customers: To ensure smooth and secure transactions.

**1 KPI for Success:** Reduction in fraud loss percentage.

## 2. Data Collection & Preprocessing

**2 Data Sources:**
- Historical transaction data from banks.
- Public datasets like Kaggle's Credit Card Fraud Detection dataset.

**1 Potential Bias:** Transaction bias if data is dominated by high-value transactions or specific regions.

**3 Preprocessing Steps:**
- Handle missing values using mean imputation for numerical features.
- Normalize features using StandardScaler.
- Encode categorical variables with one-hot encoding.

## 3. Model Development

**Model Choice:** Random Forest Classifier, chosen for its ability to handle imbalanced data and provide feature importance.

**Data Split:** 70% train, 15% validation, 15% test.

**2 Hyperparameters:** n_estimators (number of trees) to improve accuracy; max_depth to control overfitting.

## 4. Evaluation & Deployment

**2 Evaluation Metrics:** Precision to measure false positives; Recall to measure missed frauds.

**Concept Drift:** Shifts in transaction patterns; monitor with statistical tests and retrain models periodically.

**1 Technical Challenge:** Real-time processing latency; mitigate with optimized models and edge computing.
