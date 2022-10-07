import pymongo

# baglanma islemi
myClient = pymongo.MongoClient('mongodb://localhost:27017')

# database e gimre
mydb = myClient['Deneme']

myCollection = mydb['Products']

# delete_one, delete_many

for i in myCollection.find():
    print(i)

print('*'*50)

# basta querti veriyoruz
myCollection.delete_one({'name':'taha'})

# coklu silme
myCollection.delete_many({
    'name':{
        '$regex':'^I'}
})

# I ile baslayanları sil

myCollection.delete_many({})
# hepsini siler :)

for i in myCollection.find():
    print(i)