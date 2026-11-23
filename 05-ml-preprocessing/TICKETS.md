# Sprint Tickets: Preprocessing for ML

**Assignee:** Arun Gupta  
**Reviewer / Instructor:** Ronit

---

## TL-PRP-501: Leak-Free Train/Test Scaler (Standard & MinMax)
**Story Points:** 3 | **Timebox:** 20 mins | **File:** `starter_prep.py`

Implement `fit_standard_scaler(train_vals)`, `transform_standard_scaler(vals, mean, std)`, and `minmax_scale(train_vals, test_vals)`:
- Fit scaling parameters (`mean`, `std`, `min`, `max`) **only on `train_vals`**, then transform `test_vals` to prevent data leakage!

---

## TL-PRP-502: Nominal One-Hot & Ordinal Encoder
**Story Points:** 3 | **Timebox:** 20 mins | **File:** `starter_prep.py`

Implement `one_hot_encode(values, categories)` and `ordinal_encode(values, ordered_levels)`:
- `one_hot_encode`: return binary vectors (e.g. `city` -> `[1, 0, 0]`).
- `ordinal_encode`: map `["Low", "Medium", "High"]` -> `0, 1, 2`.

---

## TL-PRP-503: Date Parts, Ratios & Log1p Feature Engineering
**Story Points:** 5 | **Timebox:** 20 mins | **File:** `starter_prep.py`

Implement `engineer_features(records)`:
- Extract `list_month` and `list_dayofweek` (0=Mon .. 6=Sun) from `listing_date`.
- Compute `sqft_per_bedroom = area_sqft / bedrooms`.
- Compute `log_price = math.log1p(price_lakhs)` for right-skewed target normalization.
