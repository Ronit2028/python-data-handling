import pandas as pd
data = pd.read_csv('D:/Python Data Handling TL/python-data-handling/02-data-cleaning/data/messy_housing_deals.csv')
print(data)

q1 = data['price_lakhs'].quantile(0.25)
q3 = data['price_lakhs'].quantile(0.75)
IQR = q3-q1
lower_bound = q1-(1.5*IQR)
upper_bound = q3-(1.5*IQR)
outliers = data[(data['price_lakhs']<lower_bound) | (data['price_lakhs']>upper_bound)]
print('Q1',q1)
print('Q3',q3)
print('IQR',IQR)
print('Lower bound',lower_bound)
print('Upper bound', upper_bound)
print(outliers)