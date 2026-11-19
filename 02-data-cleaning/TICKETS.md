# Sprint Tickets: Data Cleaning ("Garbage In, Garbage Out")

**Assignee:** Arun Gupta  
**Reviewer / Instructor:** Ronit

---

## TL-CLN-201: Missing Value Audit & Imputation
**Story Points:** 2 | **Timebox:** 15 mins | **File:** `starter_cleaning.py`

Implement `count_missing(records)` and `impute_missing_numeric(values, strategy="median")` + `impute_missing_category(values, constant=None)`:
- Treat `None`, `""`, and `"N/A"` (case-insensitive) as missing.
- Numeric imputation supports `"mean"` and `"median"`.
- Categorical imputation uses `constant` if provided, otherwise the most frequent value (mode).

**Acceptance Criteria:**
- Detects missing counts in `messy_housing_deals.csv` (`city`: 1, `condition`: 1, `area_sqft`: 1, `bedrooms`: 1).
- Median imputation returns `1320.0` for `[1000, 1320, 9999, None]`.

---

## TL-CLN-202: Deduplication & String-to-Number Normalization
**Story Points:** 3 | **Timebox:** 20 mins | **File:** `starter_cleaning.py`

Implement `deduplicate_rows(records)`, `clean_category(text)`, and `parse_messy_number(text)`:
- `deduplicate_rows` removes exact duplicate rows while preserving original order.
- `clean_category` strips whitespace and converts to Title Case (`" mumbai "` -> `"Mumbai"`).
- `parse_messy_number` converts `"$1,200"`, `"1,450"`, and `"980 sqft"` into floats (`1200.0`, `1450.0`, `980.0`), returning `None` for `"N/A"` or `""`.

**Acceptance Criteria:**
- `messy_housing_deals.csv` shrinks from 22 rows to 20 unique rows.
- All currency/unit strings parse cleanly to `float`.

---

## TL-CLN-203: IQR Outlier Detection & Regression Slope Impact
**Story Points:** 5 | **Timebox:** 25 mins | **File:** `starter_cleaning.py`

Implement `iqr_outliers(values)` and `ols_slope(x, y)`:
- Compute `Q1`, `Q3`, `IQR`, `lower_fence = Q1 - 1.5 * IQR`, `upper_fence = Q3 + 1.5 * IQR`, and return flagged outliers.
- Compute OLS slope `sum((x - mx)*(y - my)) / sum((x - mx)**2)` to observe how a single outlier (`price_lakhs = 999.0`) tilts the regression line!

**Acceptance Criteria:**
- Flags `999.0` as an upper outlier in `messy_housing_deals.csv`.
- Demonstrates that removing the `999.0` outlier changes the `area_sqft -> price_lakhs` slope significantly.
