
import pandas as pd


df = pd.read_csv('sales_data_sample.csv',encoding='ISO-8859-1')
df = pd.read_json('person.json')

print(df)

