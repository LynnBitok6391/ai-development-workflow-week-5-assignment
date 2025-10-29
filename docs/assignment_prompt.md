AI Development Workflow Assignment — Full Task

Course: AI for Software Engineering
Duration: 7 days
Deliverables: PDF report (5–10 pages) + GitHub repo with code and documentation
Submit: PDF as an article in the PLP Academy Community and push code to GitHub.

Objective: Apply the AI Development Workflow to a real-world problem, show technical knowledge and ethical thinking.

PART 1 — Short Answer Questions (30 points)

1. Problem Definition (6 pts)

Define a hypothetical AI problem (one sentence).

List 3 objectives for the project.

List 2 stakeholders.

Propose 1 KPI for success.

2. Data Collection & Preprocessing (8 pts)

Identify 2 data sources (where to get the data).

Explain 1 potential bias in the data.

Outline 3 preprocessing steps you will perform.

3. Model Development (8 pts)

Choose a model and justify your choice (1–2 sentences).

Describe how to split data into train/validation/test (percentages).

Name 2 hyperparameters you will tune and why.

4. Evaluation & Deployment (8 pts)

Select 2 evaluation metrics and explain their relevance.

Define concept drift and how you will monitor for it post-deployment.

Describe 1 technical deployment challenge and a mitigation.

PART 2 — Case Study Application (40 points)

Scenario: Hospital wants an AI system to predict patient readmission risk within 30 days.

Tasks

A. Problem Scope (5 pts)

Define problem (1 sentence), list 3 objectives and 2 stakeholders.

B. Data Strategy (10 pts)

Propose data sources (EHRs, lab results, demographics, etc.).

Identify 2 ethical concerns (e.g., privacy, bias).

Design a preprocessing pipeline with feature engineering steps.

C. Model Development (10 pts)

Choose a model and justify it.

Provide a hypothetical confusion matrix and compute precision and recall.

D. Deployment (10 pts)

Outline steps to integrate the model into hospital systems (APIs, dashboards).

Explain how to ensure healthcare compliance (e.g., HIPAA) in one paragraph.

E. Optimization (5 pts)

Propose 1 method to address overfitting (e.g., cross-validation, regularization).

PART 3 — Critical Thinking (20 points)

Ethics & Bias (10 pts)

Explain how biased training data could affect patient outcomes.

Suggest 1 strategy to mitigate bias.

Trade-offs (10 pts)

Discuss interpretability vs accuracy in healthcare (short paragraph).

Explain how limited compute resources affect model choice.

PART 4 — Reflection & Workflow Diagram (10 points)

Reflection (5 pts)

What was most challenging? How would you improve with more resources?

Diagram (5 pts)

Create a simple flowchart (draw.io or PowerPoint) containing: Problem definition → Data collection → Preprocessing → Model development → Evaluation → Deployment → Monitoring.

✅ How to complete the assignment — step-by-step (do these in VS Code locally)
Setup (one-time)

Create folder ai-development-workflow and open in VS Code.

In VS Code Terminal:

python -m venv venv
# activate venv
# Windows (PowerShell):
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate
pip install scikit-learn pandas matplotlib seaborn notebook
pip freeze > requirements.txt


Create folders and files (use Explorer → New File):

ai-development-workflow/
├─ docs/
│   ├─ assignment_prompt.md   # paste this prompt into it
│   ├─ part1_short_answers.md
│   ├─ part2_case_study.md
│   ├─ part3_critical_thinking.md
│   ├─ part4_reflection.md
│   └─ final_report.md
├─ src/
│   ├─ preprocess_example.py
│   ├─ model_example.py
│   └─ evaluation_example.py
└─ requirements.txt
