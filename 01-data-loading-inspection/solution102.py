import pandas as pd
data = pd.read_csv('D:/Python Data Handling TL/python-data-handling/01-data-loading-inspection/data/properties.csv')
print(data)
print(data.isna().sum())
print(data.shape)
print(data.isna().sum())
print(data.nunique())