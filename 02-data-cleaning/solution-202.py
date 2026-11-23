import pandas as pd
data = pd.read_csv('D:/Python Data Handling TL/python-data-handling/02-data-cleaning/data/messy_housing_deals.csv')
print(data)
print('Before',len(data))
data = data.drop_duplicates()
print('After',len(data))
data['city'] = data['city'].str.strip().str.title()
print(data['city'])