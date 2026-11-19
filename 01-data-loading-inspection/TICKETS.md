# Sprint Tickets: Data Loading & First-Look Inspection

**Assignee:** Arun Gupta  
**Reviewer / Instructor:** Ronit

---

## TL-DATA-101: Multi-Format Data Ingestion (CSV, Excel, JSON)
**Story Points:** 2 | **Timebox:** 15 mins | **File:** `starter_assignment.py`

Load all three raw data sources from `data/` and verify their record counts:
1. `load_csv_records(path)` -> list of dicts from `data/properties.csv`
2. `load_json_records(path)` -> list of dicts from `data/agents.json`
3. `load_excel_sheet(path, sheet_name="Q4_Sales")` -> list of dicts from `data/sales_records.xlsx`

**Acceptance Criteria:**
- `properties.csv` loads 20 records with 10 columns each.
- `agents.json` loads 5 agent records.
- `sales_records.xlsx` (`Q4_Sales` sheet) loads 10 closed sale records.

---

## TL-DATA-102: First-Look Sanity Audit
**Story Points:** 3 | **Timebox:** 20 mins | **File:** `starter_assignment.py`

Implement `sanity_audit(records)` to mirror pandas `.shape`, `.isna().sum()`, and `.nunique()`:
- Return `shape`: `(num_rows, num_cols)`
- Return `missing_counts`: dict mapping each column name to count of empty/`None` values
- Return `nunique`: dict mapping each column name to count of distinct non-empty values
- Return `id_like_columns`: list of columns where `nunique == num_rows` (every row is unique)

**Acceptance Criteria:**
- Correctly detects `area_sqft` (1 missing) and `age_years` (1 missing) in `properties.csv`.
- Flags `property_id` and `agent_notes` as unique-per-row (`nunique == 20`).

---

## TL-DATA-103: Column Type Classifier & ML Readiness Gate
**Story Points:** 3 | **Timebox:** 20 mins | **File:** `starter_assignment.py`

Implement `classify_column_role(col_name)` and `prepare_ml_columns(records, target_col="price_lakhs")`:
- Classify every column in `properties.csv` into one of:
  `"continuous"`, `"discrete"`, `"nominal"`, `"ordinal"`, `"datetime"`, `"id"`, `"text"`
- `prepare_ml_columns(...)` must return `(feature_cols, dropped_cols, target_col)` where:
  - `id`, `text`, and raw `datetime` columns are placed in `dropped_cols` (since ML regression cannot use raw IDs, free text, or unparsed date strings directly).
  - Numeric and categorical feature columns remain in `feature_cols` (excluding `target_col`).

**Acceptance Criteria:**
- `property_id`, `agent_id`, `agent_notes`, and `listing_date` are excluded from raw ML features.
- `area_sqft`, `bedrooms`, `age_years`, `city`, and `condition` are retained for encoding/scaling.
