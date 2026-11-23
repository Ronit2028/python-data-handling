"""
TechLearns AI/ML — Exploratory Data Analysis & Summary Stats
Instructor: Ronit | Student: Arun Gupta
"""
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).parent / "data" / "housing_eda.csv")

# 1. DISTRIBUTIONS: MEAN vs MEDIAN, STD, IQR
print("Mean price_lakhs  :", round(df["price_lakhs"].mean(), 2))
print("Median price_lakhs:", round(df["price_lakhs"].median(), 2))
print("Std dev           :", round(df["price_lakhs"].std(), 2))
q1, q3 = df["price_lakhs"].quantile([0.25, 0.75])
print(f"Q1={q1:.2f}, Q3={q3:.2f}, IQR={q3 - q1:.2f}")

# 2. GROUPING & SLICING
print("\nListing counts by city:\n", df["city"].value_counts())
print("\nAverage price by city:\n", df.groupby("city")["price_lakhs"].mean().sort_values(ascending=False))

pivot = df.pivot_table(
    values="price_lakhs",
    index="city",
    columns="neighborhood_tier",
    aggfunc="mean",
)
print("\nPivot table (mean price_lakhs):\n", pivot.round(1))

# 3. RELATIONSHIPS & MULTICOLLINEARITY
corr = df[["area_sqft", "carpet_sqft", "bedrooms", "price_lakhs"]].corr()
print("\nPearson Correlation Matrix:\n", corr.round(3))
# Notice area_sqft <-> carpet_sqft has r = 1.000 (multicollinearity!)
