from cProfile import label
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

"""
x = [1,2,3,4]
y = [1,4,9,16]

# plt.plot(x, y, color='green', linewidth = '5')

plt.plot(x, y, 'o--g') # gragigin bilgileri stup i

plt.axis([0,6,0,20]) # eksenlerin degerlerini beilrliyoruz

plt.title('Grafik')
plt.ylabel('Y ekseni')
plt.xlabel('X ekseni')

plt.show() # diagrami gosterir

"""


"""

x = np.linspace(0,2,100)

plt.plot(x,x, label = "Lineer")
plt.plot(x,x**2,label = "Karesel")
plt.plot(x,x**3,label = "Kubik")

plt.title('Grafik')
plt.xlabel('X ekseni')
plt.ylabel('Y ekseni')

plt.legend() # legendi gosterir

plt.show() # diagrami gosterir

"""

"""

x = np.linspace(0,2,100)

fig , axs = plt.subplots(3)

axs[0].plot(x,x,color='red')


axs[1].plot(x,x**2,color='green')


axs[2].plot(x,x**3,color='yellow')


plt.tight_layout() # sigdirmaya yariyor hepsini

plt.show()

"""

"""

x = np.linspace(0,2,100)

fig,axs = plt.subplots(2,2)

fig.suptitle("Grafik")
axs[0,0].plot(x,x,color='red')
axs[0,1].plot(x,x**2,color='blue')
axs[1,0].plot(x,x**3,color='green')
axs[1,1].plot(x,x**4,color='yellow')

plt.show()



"""

"""
plt.subplot(2,1,1)
x = np.linspace(0,10)
y1 = np.sin(x)
plt.plot(x,y1)

plt.subplot(2,1,2)
y2 = np.sin(5*x)
plt.plot(x,y2)

plt.show()
"""

# Basic Ornek

import pandas as pd

df = pd.read_csv(r'C:\Users\90543\Desktop\VS\python\data-analysis(pandas)\nba.csv') # your data path

df = df.drop('Number',axis=1).groupby('Team').mean()

df.plot(subplots=True)

plt.legend()
plt.show()
