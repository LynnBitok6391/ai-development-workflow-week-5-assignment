# AI Development Workflow Assignment

This project contains the completed assignment for the AI Development Workflow course. It includes short answers, a case study, critical thinking questions, and example Python code demonstrating key concepts in AI model development, focusing on fraud detection.

## Project Structure

- `docs/`: Contains markdown files with assignment answers.
  - `part1_short_answers.md`: Short answer questions on problem definition, data collection, model development, and evaluation.
  - `part2_case_study.md`: Case study application in healthcare (readmission prediction).
  - `part3_critical_thinking.md`: Critical thinking on ethics, bias, and trade-offs.
  - `part4_reflection.md`: Reflection and workflow diagram.
  - `final_report.md`: Compiled final report.
- `src/`: Example Python scripts.
  - `preprocess_example.py`: Demonstrates data preprocessing (handling missing values, encoding, scaling).
  - `model_example.py`: Shows model training with Random Forest for fraud detection.
  - `evaluation_example.py`: Illustrates model evaluation with metrics and confusion matrix.
- `assignment_prompt.md`: The original assignment prompt.

## Setup Instructions

1. Ensure Python 3.8+ is installed.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install pandas scikit-learn
   ```

## Running the Examples

Navigate to the project root and run the scripts:

- Preprocessing: `python src/preprocess_example.py`
- Model Training: `python src/model_example.py`
- Evaluation: `python src/evaluation_example.py`

The scripts use sample data for fraud detection and output results to the console. Note: Warnings may appear due to small sample size, but the code demonstrates the concepts.

## Assignment Overview

The assignment covers the end-to-end AI development workflow:
- Problem scoping and stakeholder identification
- Data collection, preprocessing, and ethical considerations
- Model selection, training, and hyperparameter tuning
- Evaluation metrics and deployment strategies
- Handling bias, interpretability trade-offs, and monitoring for concept drift

All parts are completed in the docs folder, with code examples in src.
