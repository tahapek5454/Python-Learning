from unittest import result
import pandas as pd
import numpy as np


df = pd.read_csv('nba.csv')

df.dropna(inplace=True)

result = df

result = df.columns

result = df

# df['Name'] = df['Name'].str.upper() # isim stunun kompile buyuk yapar

df['index'] = df['Name'].str.find('a') # karakterini gordugu yerin indexini yeni bir stuna atıocaz

# not ->    df['Name'] == df.Name
result = df
result = df[(df.Name.str.contains('Jordan'))]

result[['FirstName','LastName']] = result['Name'].loc[result['Name'].str.split().str.len()==2].str.split(expand=True)
# zor bir bolme islemi


print(result.head())