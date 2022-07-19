from unittest import result
import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)

df = pd.DataFrame(data=data,columns=["Column1","Column2","Column3","Column4","Column5"])

result = df

result = df.columns

result = df.head() # ilk 5 ini getirir

result = df.head(10)

result = df.tail() # sondan gelir

result = df['Column1'].head() # ilgili kolunu getirir

result = df [['Column1','Column2']].head() # iligli kolanlari

result = df [5:10][['Column1',"Column2"]] # ilgili satir ve stun

# filtreleme

result = df > 50 #50 den buyuklere true koyar

result = df[df > 50] # 50 den buyukleri gosterir

result = df["Column1"] > 20 # column 1 deki degerler icin

result = df[df["Column1"] > 70]
result = df[df["Column1"] > 70]['Column1'] # ilgili column gelsin
 
result = df[(df["Column1"] > 70) & (df["Column1"] < 90)]['Column1'] # ilgili column gelsin

result = df[(df["Column1"] > 70) | (df["Column2"] > 50)]

result = df.query("Column1 > 50 & Column2 < 50") # query seklinde

result = df.query("Column1 > 50 & Column2 < 50")[['Column1','Column2']]

print("*"*50)
print(result)
print("*"*50)