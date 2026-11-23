import pandas as pd
#data = pd.read_csv('D:/Python Data Handling TL/python-data-handling/01-data-loading-inspection/data/sales_records.xlsx')
data = pd.read_csv('D:/Python Data Handling TL/python-data-handling/01-data-loading-inspection/data/properties.csv')
print(data.head())

data1 = pd.read_excel('D:/Python Data Handling TL/python-data-handling/01-data-loading-inspection/data/sales_records.xlsx',sheet_name='Q4_Sales')
print(data1.head())

data2 = pd.read_json('D:/Python Data Handling TL/python-data-handling/01-data-loading-inspection/data/agents.json')
print(data2.head())