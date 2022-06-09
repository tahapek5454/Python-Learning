
from itertools import count


list = [1,2,3]

tuple = (1,2,3,2)

print(type(list))
print(type(tuple))

print(tuple[2])

print(len(tuple))


# tuple bastaki tanımladamadan sonra elemanları degistirmemize izin vermez

# tuple[2] = 'ali'  yapamazsin hata verir

print(tuple.count(2)) # 2 listede kac kez tekrarlanıyor

print(tuple.index(2)) # 2 nin indexini donduur

tuple2 = ('ali','ahmet')

tuple = tuple + tuple2

print(tuple)


