"""
TechLearns AI/ML — Data Cleaning ("Garbage In, Garbage Out")
Instructor: Ronit | Student: Arun Gupta

Run in an environment with pandas & numpy installed:
    python3 code_samples.py
"""
from pathlib import Path
import numpy as np
import pandas as pd

DATA_PATH = Path(__file__).parent / "data" / "messy_housing_deals.csv"

# ============================================================================
# 1. LOAD MESSY DATA & CHECK MISSING VALUES + DUPLICATES
# ============================================================================
df = pd.read_csv(DATA_PATH, na_values=["", "N/A", "null"])
print("Raw shape:", df.shape)
print("Duplicate rows:", df.duplicated().sum())
print("\nMissing values per column:\n", df.isna().sum())

# Drop exact duplicate rows first
df = df.drop_duplicates().reset_index(drop=True)
print("\nShape after drop_duplicates:", df.shape)

# ============================================================================
# 2. FIX FORMATTING BUGS (WHITESPACE, CASING & NUMBERS STORED AS STRINGS)
# ============================================================================
for col in ["city", "condition"]:
    df[col] = df[col].astype("string").str.strip().str.title()

# Convert "1,450", "980 sqft" -> float
df["area_sqft"] = (
    df["area_sqft"]
    .astype("string")
    .str.replace(",", "", regex=False)
    .str.replace("sqft", "", regex=False)
    .str.strip()
)
df["area_sqft"] = pd.to_numeric(df["area_sqft"], errors="coerce")

# Convert "$1,200" -> 1200.0
df["broker_fee"] = (
    df["broker_fee"]
    .astype("string")
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)
df["broker_fee"] = pd.to_numeric(df["broker_fee"], errors="coerce")

# ============================================================================
# 3. IMPUTE MISSING VALUES (MEDIAN FOR SKEWED NUMERIC, MODE/CONSTANT FOR CAT)
# ============================================================================
df["area_sqft"] = df["area_sqft"].fillna(df["area_sqft"].median())
df["bedrooms"] = df["bedrooms"].fillna(df["bedrooms"].median())
df["city"] = df["city"].fillna(df["city"].mode()[0])
df["condition"] = df["condition"].fillna("Unknown")

# ============================================================================
# 4. DETECT OUTLIERS (IQR) & SEE HOW 1 OUTLIER TILTS LINEAR REGRESSION!
# ============================================================================
q1 = df["price_lakhs"].quantile(0.25)
q3 = df["price_lakhs"].quantile(0.75)
iqr = q3 - q1
upper_fence = q3 + 1.5 * iqr
print(f"\nPrice Q1={q1:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}, Upper Fence={upper_fence:.2f}")
print("Flagged price outliers:\n", df[df["price_lakhs"] > upper_fence][["deal_id", "city", "area_sqft", "price_lakhs"]])

# Compare OLS slope (area_sqft -> price_lakhs) WITH vs WITHOUT the 999.0 outlier
slope_with_outlier = np.polyfit(df["area_sqft"], df["price_lakhs"], 1)[0]
clean_df = df[df["price_lakhs"] <= upper_fence]
slope_clean = np.polyfit(clean_df["area_sqft"], clean_df["price_lakhs"], 1)[0]

print(f"\nRegression slope WITH 999.0 outlier   : {slope_with_outlier:.4f} lakhs/sqft")
print(f"Regression slope WITHOUT 999.0 outlier: {slope_clean:.4f} lakhs/sqft")
