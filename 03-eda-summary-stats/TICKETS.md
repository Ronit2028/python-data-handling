# Sprint Tickets: EDA & Summary Statistics

**Assignee:** Arun Gupta  
**Reviewer / Instructor:** Ronit

---

## TL-EDA-301: Distribution Stats & Skewness Check
**Story Points:** 2 | **Timebox:** 15 mins | **File:** `starter_eda.py`

Implement `distribution_summary(values)`:
- Compute `mean`, `median`, `std` (sample std, `ddof=1`), `q1`, `q3`, `iqr`, and `skew_direction` (`"right"` if `mean > median`, `"left"` if `mean < median`, else `"symmetric"`).

---

## TL-EDA-302: GroupBy & Pivot Aggregation
**Story Points:** 3 | **Timebox:** 20 mins | **File:** `starter_eda.py`

Implement `value_counts(records, col)` and `groupby_mean(records, group_col, target_col)`:
- Answer: *"How does average price vary by city and by neighborhood_tier?"*
- Return a dict sorted or keyed cleanly rounded to 2 decimals.

---

## TL-EDA-303: Pearson Correlation & Multicollinearity Detector
**Story Points:** 5 | **Timebox:** 25 mins | **File:** `starter_eda.py`

Implement `pearson_r(x, y)` and `find_collinear_pairs(records, numeric_cols, threshold=0.85)`:
- Compute exact Pearson correlation `r` between `-1.0` and `1.0`.
- Flag pairs of features with `|r| >= threshold` (e.g., `area_sqft` and `carpet_sqft`) so they aren't both fed into Linear Regression!
