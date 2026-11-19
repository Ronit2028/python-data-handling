# Data Cleaning ("Garbage In, Garbage Out") — Lesson Pack

**Instructor:** Ronit  
**Student:** Arun Gupta  
**Deck:** `TechLearns_Data_Cleaning.html` / `TechLearns_Data_Cleaning.pdf`

## Folder Contents
* `data/messy_housing_deals.csv` — 22 raw rows with duplicates, missing values, messy casing/whitespace, string-formatted numbers (`"$1,200"`, `"980 sqft"`), and extreme outliers (`bedrooms=99`, `price_lakhs=999.0`)
* `code_samples.py` — Complete `pandas` + `numpy` cleaning & regression-tilt demo
* `TICKETS.md` — 3 Jira-style assignments (`TL-CLN-201` to `TL-CLN-203`) for Arun Gupta
* `starter_cleaning.py` — Starter stubs for the 3 assignment tickets
* `solutions.py` — Reference solutions for instructor review
* `test_cleaning.py` — Automated verification suite

## Quick Start
```bash
python3 -m unittest -v test_cleaning.py
```
