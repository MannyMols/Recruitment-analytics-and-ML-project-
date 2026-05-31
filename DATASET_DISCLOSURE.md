# Dataset Disclosure

## Overview

This document provides full transparency about the nature, origin, and limitations of the dataset used in this project.

---

## Dataset Origin

The dataset used in this project — `Recruitment_master.csv` and `Recruitment_ml_ready.csv` — is **entirely synthetic**.

It was programmatically generated using Python (Faker, NumPy, Pandas) to simulate a fictional staffing agency's recruitment records. No real candidate data was collected, scraped, or used at any point.

---

## Data Generation Method

- Candidate profiles were created using randomised parameters
- Placement outcomes were assigned based on engineered probability rules
- Salary figures are fictional and do not reflect real market data
- Assessment scores, satisfaction scores, and risk tiers were synthetically derived
- XGBoost model outputs (placement_risk_tier, placement_probability) were generated from the synthetic features themselves

---

## Column Reference

| Column | Description |
|--------|-------------|
| `candidate_id` | Auto-incremented unique identifier |
| `first_name`, `last_name` | Randomly generated names — not real individuals |
| `nationality` | Randomly assigned from a pool of nationalities |
| `job_function` | Randomly assigned role category |
| `seniority_level` | Entry level / Junior / Mid / Senior / Intern |
| `years_of_experience` | Generated to align with seniority level |
| `expected_salary_gbp` | Synthetic salary expectation by seniority |
| `assessment_score` | Random score 0–100 |
| `client_satisfaction_score` | Generated with correlation to salary gap and time to hire |
| `placement_risk_tier` | XGBoost model output — High Confidence / Likely / At Risk / Unlikely |
| `placement_probability` | XGBoost predicted probability (0–1) |
| `salary_gap` | Engineered feature: offered salary minus expected salary |
| `days_since_registration` | Engineered feature: days between registration and analysis date |
| `interview_efficiency` | Engineered feature: assessment score divided by interview rounds |

---

## Intended Use

This dataset and all associated analysis are intended **solely for**:

- Portfolio demonstration of data science and ML skills
- Educational purposes
- Technical skills assessment
- Non-commercial research and learning

**This dataset must not be used to:**

- Make real hiring, screening, or placement decisions about individuals
- Train production ML systems for use on real candidates
- Represent actual market statistics or industry benchmarks
- Be published as factual recruitment industry data

---

## Privacy & Compliance

As all data is entirely synthetic:

- No GDPR, UK Data Protection Act, or personal data obligations apply to this dataset
- No individuals' privacy rights are affected
- No consent was required for data collection, as no real data was collected
- The dataset contains no real personally identifiable information (PII)

---

## Contact

**Emmanuel Mologe**
MSc Internet of Things — Ulster University (2024, Distinction)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/e-3bi-mol/)
[![GitHub](https://img.shields.io/badge/GitHub-MannyMols-181717?style=flat&logo=github)](https://github.com/MannyMols)

---
