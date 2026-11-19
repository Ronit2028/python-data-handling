# Data Loading & First-Look Inspection — Lesson Pack

**Instructor:** Ronit  
**Student:** Arun Gupta  
**Deck:** `TechLearns_Data_Loading_Inspection.html` / `TechLearns_Data_Loading_Inspection.pdf`

## Folder Contents
* `data/properties.csv` — 20 property listings (`property_id`, `city`, `condition`, `area_sqft`, `bedrooms`, `age_years`, `listing_date`, `agent_id`, `agent_notes`, `price_lakhs`)
* `data/sales_records.xlsx` — Multi-sheet Excel workbook (`Q4_Sales` and `Metadata` sheets)
* `data/agents.json` — JSON array of 5 real estate agents (`agent_id`, `agent_name`, `region`, `experience_years`, `rating`)
* `code_samples.py` — Complete `pandas` reference script for loading, sanity checks, and column-type inspection
* `TICKETS.md` — 3 Jira-style assignments (`TL-DATA-101` to `TL-DATA-103`) for Arun Gupta
* `starter_assignment.py` — Starter stubs for the 3 assignment tickets
* `solutions.py` — Reference solutions for instructor review
* `test_assignment.py` — Automated verification suite

## Quick Start
1. Review `code_samples.py` in Python / Jupyter / Colab (requires `pandas` and `openpyxl`).
2. Complete the 3 tickets in `starter_assignment.py`.
3. Run the automated test suite:
```bash
python3 -m unittest -v test_assignment.py
```
