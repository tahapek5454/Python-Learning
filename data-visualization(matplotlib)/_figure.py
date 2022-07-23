import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,9,20)
y = x**3
z = x**2

# figure = plt.figure() # figure olusturur

# axes = figure.add_axes([0.1,0.1,0.8,0.8]) # axesin figrudeki yeri ve kaplayacagi alani belirledik

# axes.plot(x,y,"g")
# axes.set_xlabel('x ekseni')
# axes.set_ylabel('y ekseni')
# axes.set_title('Grafik')

# # ayni figure bir axes bir grafik daha ekleyelim

# axes2 = figure.add_axes([0.18,0.6,0.3,0.3])

# axes2.plot(x,z,"r")
# axes2.set_xlabel('x ekseni')
# axes2.set_ylabel('y ekseni')
# axes2.set_title('Grafik')





# figure2 = plt.figure()

# axes = figure2.add_axes([0.1,0.1,0.8,0.8])

# axes.plot(x,z,"r",label = 'krasel')
# axes.plot(x,y,"g",label = 'kubik')

# plt.legend(loc=3) # locatian



fig , axes = plt.subplots(ncols=1 , nrows=2 , figsize=(12,8)) # 2 satir 1 stun yani alt altda iki grafik koyacagiz

axes[0].plot(x,y,"r")
axes[0].set_title('Cube')



axes[1].plot(x,z)
axes[1].set_title('Square')

plt.tight_layout()

fig.savefig('figure1.png') # figureu kaydeder

plt.show()