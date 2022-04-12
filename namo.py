import numpy as np
import pandas as pd
from pandas import DataFrame, Series

#zcolumns = ['First Name', 'Last Name']

zendata = pd.read_csv('ZenAcc.csv')
zendata_sorted = zendata.sort_values('Full name') 
print(zendata_sorted)

msdata = pd.read_csv('MSUsers.csv')
print(msdata)

merged = pd.concat([zendata, msdata])
final_merged = merged.drop_duplicates(subset='Last name', keep=False)
print(final_merged)