"""
TechLearns AI/ML — Data Loading & First-Look Inspection (Reference Code)
Instructor: Ronit | Student: Arun Gupta

Run in an environment with pandas & openpyxl installed:
    pip install pandas openpyxl
    python3 code_samples.py
"""
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"

# ============================================================================
# 1. LOADING CSV, EXCEL, AND JSON INTO PANDAS DATAFRAMES
# ============================================================================
props_df = pd.read_csv(
    DATA_DIR / "properties.csv",
    parse_dates=["listing_date"],   # Parse date strings into datetime64
    na_values=["", "N/A", "null"],  # Treat common placeholders as NaN
)

sales_df = pd.read_excel(
    DATA_DIR / "sales_records.xlsx",
    sheet_name="Q4_Sales",          # Explicitly pick the target worksheet
)

agents_df = pd.read_json(
    DATA_DIR / "agents.json",
    orient="records",               # Standard JSON array of objects
)

print("Loaded Shapes:")
print(f"  properties.csv : {props_df.shape}")
print(f"  Q4_Sales.xlsx  : {sales_df.shape}")
print(f"  agents.json    : {agents_df.shape}")

# ============================================================================
# 2. FIRST-LOOK SANITY CHECKS
# ============================================================================
print("\n--- .head(3) ---")
print(props_df.head(3))

print("\n--- .info() ---")
props_df.info()

print("\n--- .describe(include='all') ---")
print(props_df.describe(include="all"))

print("\n--- .nunique() (Cardinality Check) ---")
print(props_df.nunique())

print("\n--- Missing Values (.isna().sum()) ---")
print(props_df.isna().sum())

# ============================================================================
# 3. UNDERSTANDING COLUMN TYPES BEFORE MODELING (REGRESSION)
# ============================================================================
COLUMN_ROLES = {
    "property_id":  "id",          # Unique identifier -> DROP before ML
    "city":         "nominal",     # Unordered category -> One-Hot Encode
    "condition":    "ordinal",     # Ordered category (Poor < Fair < Good < Excellent) -> Ordinal Encode
    "area_sqft":    "continuous",  # Measured float -> Impute + Scale
    "bedrooms":     "discrete",    # Count integer -> Numeric feature
    "age_years":    "discrete",    # Count integer -> Impute + Numeric feature
    "listing_date": "datetime",    # Timestamp -> Extract month/day_of_week, then drop raw date
    "agent_id":     "id",          # Foreign key ID -> DROP (or join agent rating first)
    "agent_notes":  "text",        # Free text -> DROP for tabular regression (needs NLP embeddings/TF-IDF)
    "price_lakhs":  "continuous",  # Target variable (y)
}

print("\n--- Column Roles ---")
for col, role in COLUMN_ROLES.items():
    print(f"  {col:<14} -> {role} (nunique={props_df[col].nunique()})")

# Why ML models fail on raw IDs & raw text:
# 1. Raw IDs ('PROP-1001') cannot be multiplied by weights w*x, and even if
#    integer-encoded (1001, 1002), the model memorizes row IDs instead of learning patterns.
# 2. Raw text ('Corner unit near metro station') has variable length and no fixed
#    numeric meaning unless converted via TF-IDF or embeddings.
usable_features = [
    c for c, r in COLUMN_ROLES.items()
    if r in {"continuous", "discrete", "nominal", "ordinal"} and c != "price_lakhs"
]
print("\nUsable ML features (after encoding/imputation):", usable_features)
