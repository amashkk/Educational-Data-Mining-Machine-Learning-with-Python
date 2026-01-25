# Educational Data Mining & Machine Learning with Python

Predicting student dropout and academic success in higher education using machine learning models.

## Overview

This project analyzes a higher education dataset to predict whether students will **Graduate**, **Dropout**, or remain **Enrolled** at the end of their course. The analysis combines exploratory data analysis, statistical testing, feature engineering, and multiple machine learning models to identify key factors influencing student outcomes.

## Dataset

- **Source**: [Higher Education Predictors of Student Retention](https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention) (Kaggle)
- **Records**: 4,424 students
- **Features**: 35 attributes including:
  - **Socio-demographic factors**: Age, marital status, parental education/occupation, tuition status
  - **Academic performance**: Curricular units enrolled, approved, grades (1st & 2nd semester)
  - **Macroeconomic indicators**: Unemployment rate, inflation rate, GDP

## Project Structure

```
.
├── Final.ipynb                    # Main Jupyter notebook with full analysis
├── dataset.csv                    # Student dataset
├── learning_dashboardFinal.html   # Interactive learning dashboard
└── README.md
```

## Methodology

### 1. Data Cleaning & Preprocessing
- Renamed columns for consistency
- Converted categorical variables to appropriate data types
- Removed 75 outlier records (graduates with zero academic activity)

### 2. Exploratory Data Analysis
- **Chi-Square Independence Tests**: Identified statistically significant categorical features
- **Spearman Correlation Analysis**: Analyzed relationships between numerical features and target
- Removed non-significant features: `Nationality`, `International`, `Educational_special_needs`

### 3. Feature Engineering
- Aggregated semester-wise academic data into averages:
  - `avg_approved` - Average curricular units approved
  - `avg_grade` - Average grade across semesters
  - `avg_enrolled`, `avg_without_evaluations`

### 4. Machine Learning Models

| Model | Balanced Accuracy | F1 Score (weighted) | AUC (OVR) |
|-------|-------------------|---------------------|-----------|
| Random Forest (tuned) | **0.7347** | 0.7788 | 0.889 |
| XGBoost (tuned) | 0.7126 | 0.7646 | 0.893 |
| SVM (tuned) | 0.7077 | 0.7541 | 0.891 |

All models used `class_weight='balanced'` or sample weights to handle class imbalance.

## Key Findings

1. **Most Important Features**: Average approved curricular units and average grades are the strongest predictors of student outcomes
2. **Dropout Indicators**: Students with near-zero course completions in early semesters are at highest risk
3. **Model Performance**: Tuned Random Forest achieved the best balanced accuracy, while all models showed strong AUC scores (~0.89)

## Requirements

```
pandas
numpy
scikit-learn
xgboost
seaborn
matplotlib
```

## Usage

1. Clone the repository
2. Install dependencies: `pip install pandas numpy scikit-learn xgboost seaborn matplotlib`
3. Open `Final.ipynb` in Jupyter Notebook or Google Colab
4. Run all cells to reproduce the analysis

## Practical Applications

- **Early Warning Systems**: Identify at-risk students in the first semester
- **Resource Allocation**: Target support services to students with low course completion rates
- **Intervention Planning**: Design remedial courses and tutoring for struggling students

## License

This project is for educational purposes.
