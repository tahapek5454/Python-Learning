from turtle import color
import matplotlib.pyplot as plt


# stackPlot

"""
year = [2010,2011,2012,2013,2014]

player1=[20,10,12,15,5]
player2=[3,5,2,0,7]
player3=[24,24,22,27,16]



plt.plot([],[],color='y',label='oyuncu1')
plt.plot([],[],color='r',label='oyuncu2')
plt.plot([],[],color='b',label='oyuncu3')

plt.stackplot(year,player1,player2,player3,colors=['y','r','b'])

plt.legend()
plt.show()

"""


# Pie grafigi

"""


goal_type = ['Serbest Vurus','Normal Gol','Penalti']
counts = [2,7,5]
colors = ['yellow','blue','red']

plt.pie(counts,labels=goal_type,colors=colors, shadow=True , explode=(0.05,0.05,0.05), autopct="%1.1f%%")

plt.show()


"""


# Bar grafigi
""" 
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)
plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç Bilgileri")
plt.show()

"""

# Histogram

yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("yaş grupları")
plt.ylabel("Kişi Sayısı")
plt.title("Histogram Grafiği")
plt.show()