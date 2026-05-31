# Business Insights & Stakeholder Briefing

**Recruitment Analytics & ML Project**  
Stakeholder Briefing | May 2026

---

## Executive Summary

Our analysis of 500 registered candidates reveals a recruitment funnel with a **strong top-of-funnel conversion rate but critical drop-offs at the quality and retention stages**. While 74% of candidates are successfully placed, fewer than half of those placements result in high client satisfaction, and our rehire pipeline is effectively empty. A predictive risk model has identified 73 candidates currently at risk of non-placement, representing an immediate revenue recovery opportunity.

---

## Stage 1 — Registration to Placement

### What The Numbers Say

> 500 registered → 370 placed  
> **74% conversion | 130 candidates lost**

**74% is a respectable industry placement rate** — the recruitment team is performing well at converting registered candidates into active placements. However the 130 unplaced candidates represent a persistent pipeline problem. These are not all new registrations — our `days_since_registration` analysis shows many have been sitting in the system for extended periods, quietly losing placement probability over time without any formal re-engagement process.

### What This Means For The Business

Every unplaced candidate is a sunk cost — time spent on CV screening, registration, assessment, and onboarding with zero revenue return. At an average placement fee of £3,500 per candidate, 130 unplaced candidates represent **£455,000 in unrealised revenue potential**.

---

## Stage 2 — Placement to High Client Satisfaction

### What The Numbers Say

> 370 placed → 215 high satisfaction (score ≥7/10)  
> **58% satisfaction conversion | 155 placements lost to mediocre outcomes**  
> 41.9% drop rate — the biggest leak in the funnel

**This is the most alarming finding in the entire analysis**. Of every 100 candidates placed, only 58 result in a client rating the experience as genuinely positive. The other 42 are technically placed but the client was not impressed enough to score above 7 out of 10. These are clients who are unlikely to return for repeat business and will not refer this recruitment agency to other organisations.

Our regression analysis identified the two primary drivers of this satisfaction gap:

1. **Salary misalignment** — `salary_gap` was the single strongest predictor of satisfaction. When a candidate is offered less than they expected, the client relationship starts on the wrong footing — the candidate is disengaged, the recruiter spends time managing expectations, and the client absorbs the tension.

2. **Time to hire** — placements that took longer had consistently lower satisfaction scores. Clients who wait longer have higher expectations and are more critical of the outcome.

### What This Means For The Business

A 41.9% drop-off at the satisfaction stage is a client retention crisis in slow motion. These 155 mediocre placements are clients who may not renew contracts, will not provide referrals, and are actively at risk of switching to a competitor agency at the next hire cycle.

---

## Stage 3 — High Satisfaction to Rehire

### What The Numbers Say

> 215 high satisfaction → 0 confirmed rehire likely  
> **100% drop rate**

**This requires immediate investigation.** The `rehire_likelihood` field returned zero confirmed “Yes” responses in the entire dataset. There are three possible explanations:

1. The rehire data has not been collected or recorded consistently — a data quality issue
2. No follow-up process exists for converting satisfied clients into repeat business
3. Satisfied clients are not being asked about future hiring needs at the right moment

### What This Means For The Business

Rehire and referral revenue is typically the most profitable segment of a recruitment agency’s income — no sales cost, reduced onboarding time, and higher trust from the client. A zero rehire pipeline means this agency is starting from scratch with every single placement cycle and leaving significant revenue on the table.

---

## Predictive Risk Model — Risk Tier vs Actual Placement

| Risk Tier | Candidates | Actually Placed | Placement Rate |
|-----------|------------|-----------------|----------------|
| High Confidence | 313 | 307 | 98.1% |
| Likely | 114 | 62 | 54.4% |
| At Risk | 67 | 1 | 1.5% |
| Unlikely | 6 | 0 | 0.0% |

**The model is working.** The gap between High Confidence (98.1% actual placement) and At Risk (1.5% actual placement) confirms that the XGBoost risk scoring is genuinely separating candidates by real placement likelihood — not random chance.

The most critical insight here is the **At Risk tier: 67 candidates, only 1 of whom was actually placed.** These 67 candidates are currently in the pipeline, registered, costing recruiter time and administration resource, but statistically will not be placed without significant intervention.

---

## Revenue Funnel Impact

| Metric | Value |
|--------|-------|
| Average placement fee | £15 *(see note below)* |
| Total placed | 370 candidates |
| Estimated total revenue | £5,592 |
| Revenue lost from 130 unplaced | £1,965 |
| Revenue at risk (73 At Risk + Unlikely) | £1,103 |
| Recovering 50% of At Risk candidates | +£551 additional revenue |

> **⚠️ Important note for stakeholders:** The average placement fee of £15 in the dataset is a synthetic data placeholder — real recruitment agency fees typically range from **£3,000–£8,000 per placement**. Substituting a realistic fee of £3,500 gives:
>
> - Total revenue: **£1,295,000**
> - Revenue lost from unplaced: **£455,000**
> - Revenue at risk: **£255,500**
> - 50% At Risk recovery: **+£127,750 additional revenue**

---

## Five Recommendations To Stakeholders

### 1. Introduce A Salary Alignment Gate At Registration 🔴 High Priority

Before a candidate enters the active pipeline, their salary expectations should be benchmarked against current market rates for their role, seniority, and location. Candidates with expectations more than 15% above market rate should be coached or flagged before recruiter time is invested. This single intervention would address the top driver of both non-placement and client dissatisfaction.

### 2. Activate The 73 At Risk Candidates Immediately 🔴 High Priority

The 73 candidates in the At Risk and Unlikely tiers are identified by name in `Recruitment_dashboard_ready.csv`. Each should be reviewed this week with a specific action — salary adjustment, skills refresh referral, or profile rework. At a realistic fee of £3,500, converting just 20 of these candidates to placements generates **£70,000 in additional revenue.**

### 3. Create A 90-Day Re-engagement Protocol 🟡 Medium Priority

Any candidate who has been registered for more than 90 days without a placement interview should automatically trigger a re-engagement workflow — a recruiter call, profile review, and updated salary expectation check. `days_since_registration` was the single strongest predictor of placement failure, meaning the current approach of leaving candidates in the system passively is actively reducing their placement probability.

### 4. Set Time-To-Hire Targets By Role Type 🟡 Medium Priority

Since `time_to_hire_days` is the second strongest driver of client satisfaction, the recruitment firm should establish internal SLA targets — for example, permanent roles filled within 21 days, contract roles within 10 days. Recruiters should be measured against these targets and client satisfaction tracked accordingly.

### 5. Build A Rehire Follow-Up Process 🟡 Medium Priority

Every placement that scores 8 or above on client satisfaction should trigger a structured follow-up at the 3-month and 6-month mark — a brief call to ask about upcoming hiring needs, request a referral, or discuss permanent conversion for contract placements. The current zero rehire pipeline represents the single largest untapped revenue opportunity in the business.

---

## Closing Statement

This analysis demonstrates that the firm’s core placement operation is functional and performing reasonably well at the top of the funnel. The business risk is concentrated at two specific points — the satisfaction gap after placement and the complete absence of a rehire pipeline. Both are addressable through process changes rather than fundamental operational restructuring. The predictive risk model now embedded in `Recruitment_dashboard_ready.csv` gives management real-time visibility of pipeline health and enables proactive intervention before revenue is lost.

---

*Analysis produced by Emmanuel Mologe | May 2026*  
*Tools: Python, Pandas, Scikit-learn, XGBoost, Matplotlib, Plotly Dash*
