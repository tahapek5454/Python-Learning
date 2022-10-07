import pymongo


# baglanma islemi
myClient = pymongo.MongoClient('mongodb://localhost:27017')

# database e gimre
mydb = myClient['Deneme']


myCollection = mydb['Products']


# find metodunu ilk parametresi bize filterleme islemi saglar
filter = {'name':'Samsung s5'}
result = myCollection.find_one(filter)
# find liste dondurur find_one rek kayıt


# simdi sorguyu id ye gore filtreleme islemi yapalım
# fakat alınan stringi object ıd ye cevirmeliyiz 
from bson.objectid import ObjectId
result = myCollection.find_one({'_id':ObjectId('634063257ff3843be4af89d4')})

# yani bizim o filterımız queyımız aslında

result = myCollection.find({
    'name':{
        "$in" : ["Samsung s5", "Samsung s6"]
    }
})
# yukarıdaki islem iste bu gelsin bu da gelsin
# in komutu yani bu listenin icine varmı
# suslu parantezlere dikkat


#  mesela simdi para icin karsilastirma yapalım

result = myCollection.find({
    'price':{
        '$gt' : 2000
    }
})
# gt : greater Than
# gte yazsak : greater than equal yani buyuk esittir
# eq yazsak da esittir anlamı tasır
# lt : less than yani 2000 den kucuk olanlar
# lte : less than equal 200 den kucuk ve esit

# Mongodb operatorlerden bakabilirz

# simdi ise regular expression baklaım

result = myCollection.find({
    'name':{'$regex':'^S'}
})
# bize s ile baslayan kayırları getir

for i in result:
    print(i)
