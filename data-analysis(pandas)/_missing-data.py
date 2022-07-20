
import pandas as pd
import numpy as np


data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data=data,index=['a','c','e','f','h'],columns=['column1',"column2","column3"])

print(df)

df = df.reindex(['a','b','c','d','e','f','g','h'])

print(df)

print('*'*50)

result = df.drop('column1',axis=1) # ilgilenmedigimiz kolonu siler

result = df.drop('a',axis=0) # iligli indexi siler

result = df.isnull() # bize null degerleri true dondurur

result  = df.isnull().sum() # bize null degerleriin sayilarini verir

result = df['column1'].isnull().sum() # ilgili kolondaki null degeri verir

newColumn = [np.nan , 30 , np.nan , 51 , np.nan , 30 , np.nan , 10]

df['column4'] = newColumn


print(df)
print('*'*50)

result = df[(df['column1'].isnull())]
result = df[(df['column1'].isnull())]['column1']

result = df[(df['column1'].notnull())]
result = df[(df['column1'].notnull())]['column1']

result = df.dropna() # axis = 0 nan olan satiri siler
result = df.dropna(axis=1) # axis = 1 nan olan stuunu siler

result = df.dropna(how='any') # herhangi bir null gorurse siler
result = df.dropna(how='all') # tum stunlar null sa siler

result = df.dropna(subset=['column1','column2'],how="any") # herhangi bir nullsa siler
result = df.dropna(subset=['column1','column2'],how="all") #ikisi birden nullsa siler

result = df.dropna(thresh=2) # en az iki normal veri olsun yoksa  sil

result = df.fillna(value=1) # doldur

result = df.sum() # stunlardaki toplam degeri verir
result = df.sum().sum() # tum toplami verir
result = df.size # eleman sayisini verir
result = df.isnull().sum() # stunlardaki null sayisini verir
result = df.isnull().sum().sum() # toplam null sayisini verir

def getMean(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet

result = df.fillna(value=getMean(df))

print(result)