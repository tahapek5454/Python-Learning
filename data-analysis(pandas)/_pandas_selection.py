import imp
import pandas as pd
from numpy.random import randn


df = pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])

print(df)
print("*"*50)

# Stunlara gore cekeceksek

print(df["Column1"])
print("*"*50)
print(type(df["Column1"]))
print("*"*50)
print(df[["Column1","Column2"]])

# Satirlara gore cekeceksek

# loc['row','column'] -> loc['row'] -> loc[:,'column']
print("*"*50)
print(df.loc["A"])
print("*"*50)
print(df.loc[:,'Column1'])

# baslangic ve bitis dahil olmak uzere

print(df.loc[:,'Column1':'Column3'])
print("*"*50)
print(df.loc[:,:])
print("*"*50)
print(df.iloc[2]) # 2 numarali index olmasa bile ilock ile sayilarla indexliymis gibi veri getirebilriz

# tek deger alma
print("*"*50)
print(df.loc['A','Column1'])

# df ye veri ekleme

df['Column4'] = pd.Series(randn(3),index=['A','B','C'])
df["Column5"] = df["Column1"]+df["Column4"]
print("*"*50)
print(df)

# kolon silme

new_df = df.drop('Column5',axis=1) # axis 1 y ekseni stundan sil dedik
print("*"*50)
print("Eski")
print(df)
print("*"*50)
print("Yeni")
print(new_df)

# Eger kopya çıkarmak istemezsek tek df uzerinde calismak istersek
df.drop('Column5',axis=1,inplace=True) # paremteryi True yapmak lazım
print("*"*50)
print("Eski")
print(df)

