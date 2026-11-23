import pandas as pd
data = pd.read_csv('D:/Python Data Handling TL/python-data-handling/02-data-cleaning/data/messy_housing_deals.csv')
print(data)
missing = ['','n/a','N/A']
data.replace(missing,pd.NA , inplace=True)
print(data.isna().sum())
data['area_sqft'] = data['area_sqft'].str.replace(',','').str.replace('sqft','').astype(float)
data['broker_fee'] = data['broker_fee'].str.replace('$','').str.replace(',','').astype(float)
print(data.info())

data["area_sqft"] = data["area_sqft"].fillna(data["area_sqft"].median())
data["bedrooms"] = data["bedrooms"].fillna(data["bedrooms"].median())
data['bedrooms'] = data['bedrooms'].fillna(data['bedrooms'].median())