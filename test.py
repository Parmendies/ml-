import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

pumpkins = pd.read_csv('US-pumpkins.csv')
pumpkins.head()
pumpkins = pumpkins[pumpkins['Package'].str.contains(
    'bushel', case=True, regex=True)]

new_columns = ['Package', 'Variety', 'City Name',
               'Month', 'Low Price', 'High Price', 'Date']
pumpkins = pumpkins.drop(
    [c for c in pumpkins.columns if c not in new_columns], axis=1)

price = (pumpkins['Low Price'] + pumpkins['High Price']) / 2

month = pd.DatetimeIndex(pumpkins['Date']).month
day_of_year = pd.to_datetime(pumpkins['Date']).apply(
    lambda dt: (dt-datetime(dt.year, 1, 1)).days)
new_pumpkins = pd.DataFrame(
    {'Month': month,
     'Variety': pumpkins['Variety'],
     'DayOfYear': day_of_year,
     'Package': pumpkins['Package'],
     'Low Price': pumpkins['Low Price'],
     'High Price': pumpkins['High Price'],
     'Price': price})

new_pumpkins.loc[new_pumpkins['Package'].str.contains(
    '1 1/9'), 'Price'] = price/1.1
new_pumpkins.loc[new_pumpkins['Package'].str.contains(
    '1/2'), 'Price'] = price*2
