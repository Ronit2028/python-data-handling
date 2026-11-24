import pandas as pd
def classify_column_role(col_name):
    # ID columns
    if col_name in ['property_id', 'agent_id']:
        return 'id'
    # Text columns
    elif col_name == 'agent_notes':
        return 'text'
    # Datetime columns
    elif col_name == 'listing_date':
        return 'datetime'
    # Continuous columns
    elif col_name in ['area_sqft', 'price_lakhs', 'age_years']:
        return 'continuous'
    # Discrete columns
    elif col_name in ['bedrooms', 'bathrooms']:
        return 'discrete'
    # Nominal columns
    elif col_name == 'city':
        return 'nominal'
    # Ordinal columns
    elif col_name == 'condition':
        return 'ordinal'
    else:
        return 'unknown'
def prepare_ml_columns(columns, target_col="price_lakhs"):
    feature_cols = []
    dropped_cols = []
    for col in columns:
        role = classify_column_role(col)
        if col == target_col:
            continue
        elif role in ['id', 'text', 'datetime']:
            dropped_cols.append(col)
        else:
            feature_cols.append(col)
    return feature_cols, dropped_cols, target_col