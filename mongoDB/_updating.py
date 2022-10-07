import pymongo

# baglanma islemi
myClient = pymongo.MongoClient('mongodb://localhost:27017')

# database e gimre
mydb = myClient['Deneme']

myCollection = mydb['Products']

# update_one, update_many

myCollection.update_one(
    {'name':'Samsung s6'},
    {'$set':{
        'name':'Iphone 7',
        'price':7000
    }}
)

# ilk parametre hangi veriye yapacagımızı seciyoruz
# ikincisinde ise set kullanarak nereyi duzeltecegimizi seciyoruz


myCollection.update_many(
    {'name':'Samsung s7'},
    {'$set':{
        'name':'Iphone 8',
        'price':7000
    }}
)
# Many de tum hepsine yapar


query = {"name":"Iphone 6"}
values = { '$set':{
    'name':'taha',
    'price':'54'
}}

result = myCollection.update_many(query, values)

print(result.modified_count)
# bana kac kayıt guncellendi soyler


for i in myCollection.find():
    print(i)
