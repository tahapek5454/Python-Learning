import pymongo

# baglanma islemi
myClient = pymongo.MongoClient('mongodb://localhost:27017')

# database e gimre
mydb = myClient['Deneme']

# collectionmuzua gecelim
myCollection = mydb["Products"]

# var olan collectionları listeleyim
print(mydb.list_collection_names())

product = {"name":"Samsung s5", "price":2000}
# verileri dict formatında olusturmalsin

result = myCollection.insert_one(product)
# tek bir veri eklemek icin isertOne

print(result)
# eklenen verinin id sini gormek istersek
print(result.inserted_id)

productList = [
    {"name":"Samsung s9", "price":2000},
    {"name":"Samsung s6", "price":4000},
    {"name":"Samsung s7", "price":6000},
    {"name":"Samsung s8", "price":8000}
]

# cogul kayıt yapmak icin many
result = myCollection.insert_many(productList)

# ekledigim verilerin idlerini gormekicin
print(result.inserted_ids)

# mesela ekledigimiz kayıtların hepsi aynı formatta olmak zorunda degiller

productList2 = [
    {"name":"iphone", "price":10000, "description":"iyi"},
    {"name":"iphone", "price":10000, "categories":['telefon', 'elektronik']},
]

result = myCollection.insert_many(productList2)
print(result.inserted_ids)
