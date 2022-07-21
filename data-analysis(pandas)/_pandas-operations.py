
import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

print(df)

print('*'*50)

result = df['Column2'].unique() # tekrarsizlar gelir
result = df['Column2'].nunique() # tekrarsizlar sayisi gelir
result = df['Column2'].value_counts() # elemanin tekrar sayisi verir

result = df['Column2'] * df['Column2']  # karesini alir

def kare(x):
    return x*x

kare2 = lambda x : x*x

result = df['Column2'].apply(kare) # apply ilgili fonksiyona tum elemanlari sirayla yoolar
result = df['Column2'].apply(kare2) # apply ilgili fonksiyona tum elemanlari sirayla yoolar
result = df['Column2'].apply(lambda x : x*x) # apply ilgili fonksiyona tum elemanlari sirayla yoolar

result = df.sort_values('Column2') # kucukten buyuye siralar
result = df.sort_values('Column2',ascending=False) # buyukten kucuge siralar


print(result)


data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)

print(df.pivot_table(index="Ay",columns= "Kategori", values= "Gelir"))