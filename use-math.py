
# 1. yontem

# import math  # as islem dersek artik ismi islem olur

# tum metodları gormek icin

# value = dir(math)

# print(value)


# bunlarla ilgili bilgi almak icin

# value = help(math)


# Ornek kullanimlar

# value = math.sqrt(49)
# print(value)

# print(math.factorial(5))
# print(math.floor(5.8)) # assagi yuvarlama
# print(math.ceil(5.8))  # yukari yuvarlama

from math import *

# bu sekilde dersek math deki her seyi import et demis oluruz
# ve artik math keywordnuu kullanmamiza gerek kalmaz

print(factorial(5))

# Not : eger ayni isimde bir fonk kullanirsam importun ustune tanımladıysam importtan gelen
# kullanilir importun altina tanımladıysam importun altındaki isleme alinir