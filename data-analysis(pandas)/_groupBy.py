
import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)

result = df
result = df['Maaş'].sum()
result = df.groupby('Departman')
result = df.groupby('Departman').groups

semtler = df.groupby('Semt')

# for name , grup in semtler:
#     print(name)
#     print('*'*50)
#     print(grup)

result = df.groupby('Semt').get_group('Kadıköy') # iligli gruplamadan iligli grubu cekme

result = df.groupby('Departman').sum() # deparmana gore gruplar numerikleri toplar

result = df.groupby('Departman').mean() # aynisiin ortalamasi

result = df.groupby('Departman')['Maaş'].mean() # hangi stunun gelcegini soyluyorsun

result = df.groupby('Semt').count() # gruplarin sayisini verir

result = df.groupby('Semt')['Çalışan'].count() # gruplarin sayisini verir

result = df.groupby('Departman')['Maaş'].max() # gruplarin max maaşı

result = df.groupby('Departman')['Maaş'].max()['Muhasebe'] # Muhasebede max maaş

result = df.groupby('Departman')['Maaş'].agg([np.mean,np.sum,np.max,np.min]) # gruplarin aggleri toplu verme

result = df.groupby('Departman')['Maaş'].agg([np.mean,np.sum,np.max,np.min]).loc['Muhasebe']


print(result)