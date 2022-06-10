
#for

list = [1,2,3,4,5,6]


for a in list:
    print(a)

name = 'taha'

for a in name:
    print(a,end=" ")  # bu ifade yan yana yazdırmayı saglar

print()

dic = {'k1':1 , 'k2':2}

print('*'*50)

for a in dic:   # sadece key i alir
    print(a)

print('*'*50)

for a in dic.items():  # key ve value alır
    print(a)

print('*'*50)

for a,b in dic.items(): #key ve value ayrı ayrı alır
    print(a)
    print(b)


# while

sayi = 0

while sayi<10:
    print(f"sayinin degeri {sayi}")
    sayi= sayi+1

print("bitti")

# kullanıcıdan onun sectigi kadar urun sayısnı bir urun fiyat key olacak sekilde listeye e at

dict = []

sayi = int(input("Urun sayisini giriniz :"))
i = 0

while i<sayi:

    urun = input("Urun ismi :")
    fiyat = int(input("Fiyat : "))

    dict.append({

        'urun' : urun ,
        'fiyat' : fiyat

    })
    i = i+1

print(dict)

