import pymongo

# baglanma islemi
myClient = pymongo.MongoClient('mongodb://localhost:27017')

# database e gimre
mydb = myClient['Deneme']

# bize databaselermizi gosterir
print(myClient.list_database_names())

myCollection = mydb['Products']

# # bize ilk bir tane kaydı getirir
# result = myCollection.find_one()

# for i in myCollection.find():
#     # bize tum kayıtları geriri
#     print(i)

for i in myCollection.find({}, {'_id':0}):
    # bu filtreleme islemi bize ilk parametere
    # tum kayıtlara bak ve id 0 yani id getirme demek
    print(i)

for i in myCollection.find({}, {'_id':0, 'name':1}):
    # bu filtreleme islemi bize ilk parametere
    # tum kayıtlara bak ve id 0 yani id getirme demek
    # spesifik isler icin de boyle yapıyoruz
    # id gelmesin name gelsin
    # id gelmesin demezsen gelir ama diğerleri gelmez
    print(i)

# print(result)