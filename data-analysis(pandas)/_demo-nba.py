import pandas as pd
import numpy as np


# 1- İlk 10 kaydı getiriniz.

df = pd.read_csv('nba.csv')

result = df.head(10)

# 2- Toplam kaç kayıt vardır ?

result = len(df.index)

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?

result = df['Salary'].mean()

# 4- En yüksek maaşı ne kadardır ?

result = df['Salary'].max()

# 5- En yüksek maaşı alan oyuncu kimdir ?

result = df[df['Salary'] == df['Salary'].max()]['Name'].iloc[0]

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.


result = df[(df['Age'] >=20) & (df['Age'] <= 25)][['Name','Team','Age']].sort_values('Age',ascending=False)

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?

result = df[df['Name'] == 'John Holland'][['Name','Team']]

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?

result = df.groupby('Team').mean()['Salary']

# 9- Kaç farklı takım mevcut ?

result = df['Team'].unique()
result = df['Team'].nunique()

# 10- Her takımda kaç oyuncu oynamaktadır ?

result = df.groupby('Team').count()['Name']
result = df['Team'].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
df.dropna(inplace=True)
result = df[df.Name.str.contains('and')]

print(result)