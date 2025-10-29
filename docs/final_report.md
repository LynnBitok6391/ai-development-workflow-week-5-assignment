# Final Report

## PART 1 — Short Answer Questions

### 1. Problem Definition

**Hypothetical AI Problem:** Develop an AI system to predict fraudulent credit card transactions in real-time.

**3 Objectives:**
- Reduce fraudulent transactions by 30% within the first year.
- Minimize false positives to avoid blocking legitimate transactions.
- Enhance security measures for financial institutions.

**2 Stakeholders:**
- Financial institutions: To protect against fraud.
- Customers: To ensure smooth and secure transactions.

**1 KPI for Success:** Reduction in fraud loss percentage.

### 2. Data Collection & Preprocessing

**2 Data Sources:**
- Historical transaction data from banks.
- Public datasets like Kaggle's Credit Card Fraud Detection dataset.

**1 Potential Bias:** Transaction bias if data is dominated by high-value transactions or specific regions.

**3 Preprocessing Steps:**
- Handle missing values using mean imputation for numerical features.
- Normalize features using StandardScaler.
- Encode categorical variables with one-hot encoding.

### 3. Model Development

**Model Choice:** Random Forest Classifier, chosen for its ability to handle imbalanced data and provide feature importance.

**Data Split:** 70% train, 15% validation, 15% test.

**2 Hyperparameters:** n_estimators (number of trees) to improve accuracy; max_depth to control overfitting.

### 4. Evaluation & Deployment

**2 Evaluation Metrics:** Precision to measure false positives; Recall to measure missed frauds.

**Concept Drift:** Shifts in transaction patterns; monitor with statistical tests and retrain models periodically.

**1 Technical Challenge:** Real-time processing latency; mitigate with optimized models and edge computing.

## PART 2 — Case Study Application

### A. Problem Scope

**Problem Definition:** Predict patient readmission risk within 30 days to improve care and reduce costs.

**3 Objectives:**
- Reduce readmission rates by 15%.
- Identify high-risk patients for early intervention.
- Optimize resource allocation in hospitals.

**2 Stakeholders:**
- Healthcare providers: To deliver targeted care.
- Hospital administrators: To manage costs.

### B. Data Strategy

**Data Sources:** Electronic Health Records (EHRs), lab results, demographics, admission/discharge data.

**2 Ethical Concerns:**
- Privacy: Protecting patient data under HIPAA.
- Bias: Ensuring data represents diverse populations to avoid discriminatory predictions.

**Preprocessing Pipeline:**
- Data cleaning: Handle missing values, normalize features.
- Feature engineering: Create age groups, comorbidity scores.
- Encoding: Convert categorical variables to numerical.

### C. Model Development

**Model Choice:** Logistic Regression for interpretability in healthcare.

**Hypothetical Confusion Matrix:**
- TP: 150, FP: 50, TN: 200, FN: 100
- Precision: TP/(TP+FP) = 150/200 = 0.75
- Recall: TP/(TP+FN) = 150/250 = 0.6

### D. Deployment

**Integration Steps:**
- Develop API for model predictions.
- Integrate into EHR systems and dashboards.
- Train staff on using the system.

**Compliance:** Ensure HIPAA compliance by encrypting data, access controls, and regular audits to protect patient privacy and prevent breaches.

### E. Optimization

**Method to Address Overfitting:** Use cross-validation to validate model performance on unseen data.

## PART 3 — Critical Thinking

### Ethics & Bias

**Impact of Biased Data:** Biased training data could lead to inaccurate predictions, disproportionately affecting minority groups, resulting in unequal healthcare access.

**Mitigation Strategy:** Use fairness-aware algorithms and diverse datasets.

### Trade-offs

**Interpretability vs Accuracy:** In healthcare, interpretability is crucial for trust and decision-making, even if accuracy is slightly lower.

**Compute Resources:** Limited resources favor simpler models like logistic regression over complex neural networks.

## PART 4 — Reflection & Workflow Diagram

### Reflection

**Challenges:** Balancing ethics with technical requirements.

**Improvements:** With more resources, conduct extensive bias testing.

### Diagram

Create a flowchart: Problem definition → Data collection → Preprocessing → Model development → Evaluation → Deployment → Monitoring.
