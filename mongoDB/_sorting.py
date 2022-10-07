from unittest import result
import pymongo

# baglanma islemi
myClient = pymongo.MongoClient('mongodb://localhost:27017')

# database e gimre
mydb = myClient['Deneme']

myCollection = mydb['Products']

result = myCollection.find().sort('name', -1)
# veriler paremetreye gore sıralama yapılır
# 2. parametreye 1 verirsen artan bir sıralama yapar -1 verirsen azalan


# coklu sıralama d su sekilde
result = myCollection.find().sort([('name', -1), ('price', -1)])
# once name gore name aynıysa price

for i in result:
    print(i)