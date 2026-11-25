import pandas as pd
sales_record = pd.read_excel('D:/Python Data Handling TL/python-data-handling/01-data-loading-inspection/data/sales_records.xlsx')
print(sales_record.head())
print(sales_record.info())
def classify_column_role(col_name):
    print('Type of columns ',col_name,'is', sales_record[col_name].dtype)
    type_of_col = sales_record[col_name].dtype
    if type_of_col == 'float64':
        return 'continous'
    elif type_of_col == 'int64':
        return 'discrete'
    elif type_of_col == 'str':
            return 'text'
    elif type_of_col == 'object':
                return 'object'
            
for col in sales_record.columns:
    role = classify_column_role(col)
    print(f'Columns: {col} , Role: {role}')

def prepare_ml_columns(columns, target_col="price_lakhs"):
    feature_cols = []
    dropped_cols = []
    for col in columns:
        role = classify_column_role(col)
        if role in ['id', 'text', 'datetime']:
            dropped_cols.append(col)
        else:
            feature_cols.append(col)
    
    return feature_cols, dropped_cols, target_col
            
            
feature_cols,dropped_cols,target_cols = prepare_ml_columns(sales_record.columns)        
print('Feature Columns',feature_cols)
print('Dropped Columns',dropped_cols)
            
    # # ID columns
    # if col_name in ['property_id', 'agent_id']:
    #     return 'id'
    # # Text columns
    # elif col_name == 'agent_notes':
    #     return 'text'
    # # Datetime columns
    # elif col_name == 'listing_date':
    #     return 'datetime'
    # # Continuous columns
    # elif col_name in ['area_sqft', 'price_lakhs', 'age_years']:
    #     return 'continuous'
    # # Discrete columns
    
    # # Nominal columns
    # elif col_name == 'city':
    #     return 'nominal'
    # # Ordinal columns
    # elif col_name == 'condition':
    #     return 'ordinal'
    # else:
    #     return 'unknown'
