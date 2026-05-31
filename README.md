# Recruitment Analytics & ML Project

A full end-to-end data science project built on a synthetic recruitment dataset for a fictional staffing agency. The project covers
data cleaning, EDA, feature engineering, ML modelling (XGBoost, Stacking Ensemble), model evaluation with SHAP,
funnel analysis, revenue impact modelling, and an interactive Plotly Dash dashboard.

Built entirely in Python using JupyterLab.

> **Not a technical reader?** If you're a recruiter or interested in the data story, head straight to the [Business Insights & Stakeholder Summary](BUSINESS_INSIGHTS.md).

---

## Project Structure

| Notebook | Purpose |
|---|---|
| `01_data_loading_and_cleaning.ipynb` | Load raw CSVs, fix dtypes, merge, handle nulls |
| `02_exploratory_data_analysis.ipynb` | Distributions, correlations, placement rate analysis |
| `03_feature_engineering.ipynb` | Feature creation, leakage removal, encode categoricals |
| `04_ml_placement_prediction.ipynb` | Binary classification — predict placement outcome |
| `05_ml_satisfaction_regression.ipynb` | Regression — predict client satisfaction score |
| `06_advanced_models.ipynb` | Advanced ML — XGBoost & Stacking Ensemble classifier, ROC-AUC evaluation |
| `07_model_evaluation.ipynb` | Deep model evaluation — SHAP explainability, cross-validation, ROC curves, confusion matrices |
| `08_dashboard_export.ipynb` | Export dashboard-ready CSV with ML predictions, placement probability & risk tier labels |
| `09_funnel_analysis.ipynb` | Recruitment funnel analysis — stage drop-off rates, seniority breakdown, revenue impact estimation |
| `10_dashboard_app.ipynb` | Interactive Plotly Dash dashboard — KPI cards, risk donut chart, seniority bar, at-risk candidate table |
| `10_dashboard_app.py` | Standalone Python script to run the Dash dashboard app locally on localhost:8050 |

---

## Dataset

Two synthetic CSV files:

- **`candidate_profiles.csv`** — 500 candidates with 19 features including 
  experience, salary expectations, skills, assessment scores, and 
  registration dates
- **`placement_outcomes.csv`** — 370 placement records with 24 features 
  including offered salary, time to hire, client satisfaction, and 
  contract details

Overall placement rate: **74%** (370 of 500 candidates placed)

> **Synthetic Data Disclosure:** This dataset was fully generated using AI (ChatGPT) from a structured prompt designed by the author. No real candidate, company, or placement data was used at any point. It is intended solely for portfolio and educational purposes. For full details, see [DATASET_DISCLOSURE.md](DATASET_DISCLOSURE.md).

---

## Key Findings

### Placement Prediction (`04_`)

Pre-hire candidate attributes alone could **not** reliably predict 
placement outcomes.

| Model | ROC-AUC | Accuracy |
|---|---|---|
| Logistic Regression | 0.5946 | 0.68 |
| Random Forest | 0.6021 | 0.74 |
| LR Balanced | 0.5967 | 0.57 |
| RF Balanced | 0.5839 | 0.74 |
| **5-Fold CV (RF)** | **0.485** | — |

Cross-validation confirmed the result is stable across all folds 
(std: 0.024), not a lucky split.

**Business insight:** Placement success is process-driven rather than 
candidate-driven. Investment in tracking process quality metrics 
(recruiter responsiveness, brief accuracy, interview feedback speed) 
would yield stronger predictive capability than additional candidate 
screening.

**Top pre-hire features by importance:**
1. `days_since_registration` — fresher candidates place faster
2. `expected_salary_gbp` — salary alignment is the strongest candidate-level signal
3. `english_proficiency` — communication ability affects client acceptance
4. `assessment_score` — internal screening quality predicts placement
5. `years_of_experience` — experience helps but less than the above four

---

### Satisfaction Regression (`05_`)

Predicting `client_satisfaction_score` (1–10 scale) for the 370 placed 
candidates using both pre and post-placement features.

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 1.8778 | 2.2324 | 0.1765 |
| Ridge | 1.8785 | 2.2326 | 0.1764 |
| Random Forest | 1.8247 | 2.2192 | 0.1863 |
| Gradient Boosting | 1.8520 | 2.2657 | 0.1518 |
| **5-Fold CV (RF)** | — | — | **0.068** |

**Top drivers of client satisfaction:**
1. `salary_gap` — the gap between offered and expected salary is the 
   dominant predictor. Clients who meet or exceed salary expectations 
   report significantly higher satisfaction
2. `time_to_hire_days` — faster placements consistently yield higher 
   satisfaction scores
3. `assessment_score` and `english_proficiency` — candidate quality 
   metrics carry into post-placement outcomes

**Business recommendation:** Hire Hangar should prioritise salary 
alignment coaching for candidates and set internal targets for 
time-to-hire to directly improve client satisfaction scores.

---

## Methodology Notes

### Data Leakage — A Core Focus

A significant part of this project involved identifying and removing 
data leakage across multiple iterations. Starting from a misleading 
ROC-AUC of 1.0, the following post-placement columns were 
systematically identified and removed from the placement prediction model:

| Column | Reason removed |
|---|---|
| `offered_salary_gbp` | Only exists after placement |
| `time_to_hire_days` | Only exists after placement |
| `interview_rounds` | Only exists after placement |
| `client_satisfaction_score` | Post-placement outcome |
| `performance_rating` | Post-placement review |
| `interview_efficiency` | Derived from post-placement data |
| `contract_type` | From `placement_outcomes.csv` |
| `placement_region` | From `placement_outcomes.csv` |
| `client_industry` | From `placement_outcomes.csv` |

Cross-validation was used at the end of each notebook to confirm that 
reported scores reflect genuine generalisation rather than test set luck.

---

## Tech Stack

| Tool | Use |
|---|---|
| Python 3 | Core language |
| pandas | Data manipulation |
| numpy | Numerical operations |
| scikit-learn | ML models, scaling, evaluation |
| matplotlib / seaborn | Visualisation |
| JupyterLab | Development environment |

---

## How To Run

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/hire-hangar-analytics.git
cd hire-hangar-analytics

# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn jupyterlab

# Launch JupyterLab
jupyter lab

# Run notebooks in order: 01 → 02 → 03 → 04 → 05
```

Each notebook from `02_` onwards loads from saved CSV files 
(`hire_hangar_master.csv`, `hire_hangar_ml_ready.csv`) produced 
by the previous notebook, so they must be run in sequence.

---

## Author

**Emmanuel Mologe**  
MSc Internet of Things — Ulster University (2024, Distinction)  
Data Analyst | Machine Learning | Python | SQL | Power BI  
[LinkedIn](https://linkedin.com/in/emmanuel-mologe) | 
[GitHub](https://github.com/MannyMols)
