import pandas as pd


data = [['ahmet',50],["Mehmet",30],["asli",45]]

df = pd.DataFrame(data=data)
print(df)

print("*"*50)

df = pd.DataFrame(data=data , columns=["name","score"],index=[1,2,3])
print(df)

print("*"*50)

dictt = {"Name":["ali","ayse"] , "Score" : [10,20]}

df = pd.DataFrame(data=dictt , index=[1,2])

print(df)

print("*"*50)

dict_liste = [

    {"Name": "Ahmet" , "Score" : 20},
    {"Name": "Mehmet" , "Score" : 40},
    {"Name": "Asli" , "Score" : 50},
    {"Name": "Taha" , "Score" : 20},
    {"Name": "Sila" , "Score" : 10}
]

df = pd.DataFrame(dict_liste)

print(df)

print("*"*50)

s1 = [0,1,2,3]
s2 = [5,6,7,8]

data = dict(apple=s1, banana = s2)

df = pd.DataFrame(data)

print(df)