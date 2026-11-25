import pandas as pd
#data = pd.read_csv('D:/Python Data Handling TL/python-data-handling/01-data-loading-inspection/data/sales_records.xlsx')
data = pd.read_csv('D:/Python Data Handling TL/python-data-handling/01-data-loading-inspection/data/properties.csv')
print(data.head())

data = pd.read_excel('D:/Python Data Handling TL/python-data-handling/01-data-loading-inspection/data/sales_records.xlsx',sheet_name='Q4_Sales')
print(data.head())
data = pd.read_json('D:/Python Data Handling TL/python-data-handling/01-data-loading-inspection/data/agents.json')

print(data.shape)

print(data.head(3))
print(data.info())
print(data.isna().sum())
print(data.nunique())