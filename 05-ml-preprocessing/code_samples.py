"""
TechLearns AI/ML — Preprocessing: The Bridge from Data to ML
Instructor: Ronit | Student: Arun Gupta

Run in an environment with pandas, numpy & scikit-learn installed:
    python3 code_samples.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge

df = pd.read_csv(Path(__file__).parent / "data" / "house_ml_prep.csv", parse_dates=["listing_date"])

# 1. BASIC FEATURE ENGINEERING (row-wise, safe before split)
df["list_month"] = df["listing_date"].dt.month
df["list_dow"] = df["listing_date"].dt.dayofweek
df["sqft_per_bedroom"] = df["area_sqft"] / df["bedrooms"]
y = np.log1p(df["price_lakhs"])  # Log transform right-skewed target

X = df[["city", "condition", "area_sqft", "bedrooms", "list_month", "list_dow", "sqft_per_bedroom"]]

# 2. TRAIN/TEST SPLIT *BEFORE* ANY FITTING (PREVENT DATA LEAKAGE!)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. ENCODING + SCALING VIA COLUMNTRANSFORMER
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["area_sqft", "bedrooms", "list_month", "list_dow", "sqft_per_bedroom"]),
        ("nom", OneHotEncoder(drop="first", handle_unknown="ignore"), ["city"]),
        ("ord", OrdinalEncoder(categories=[["Low", "Medium", "High"]]), ["condition"]),
    ]
)

model = Pipeline([("prep", preprocessor), ("reg", Ridge(alpha=1.0))])
model.fit(X_train, y_train)
print("Train R2 (log target):", round(model.score(X_train, y_train), 4))
print("Test  R2 (log target):", round(model.score(X_test, y_test), 4))
