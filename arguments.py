

import email


def changeName(n):
    n = 'pek'

name = 'taha'

changeName(name)

print(name)

# degismedi cunku value tipte degiskenler referans olsa degisirdi

def change_list(liste):
    liste[0]="sakarya"

liste=["ankara","istanbul"]

#change_list(liste)

#print(liste)

# degisti cunku referans tipi 

# referans degiskligi istemiyorsak eger listeyi baska bir listeye kopyalamalıyız

copy_liste = liste[:]  # slicing islemi

change_list(copy_liste)

print(copy_liste)
print(liste)

def add (*params):    ## bu sekilde sinirsiz parametre alabiliyor * tuple yapar
    return sum((params))   # python  kutuphanesinde gelen bir fonksiyon

toplam = add(1,2)

print(f"toplama sonucu : {toplam}")

toplam = add(1,2,3)

print(f"toplama sonucu : {toplam}")

toplam = add(1,2,3,4)

print(f"toplama sonucu : {toplam}")


# ben karmasik parametre yollayacaksam mesela string integer tipi falan dict kullanmaliyim

def display(**args): # ** dict gelecegini bildirir
    print(type(args))
    print(args)
    print("*"*50)
    for key,value in args.items():
        print(f"{key} == {value}")


display(name='taha',age=18)
display(name='arda',age=25,email='arda@gmail.com')


def my_function (a, b, *listem, **dictonarym):
    print(a)
    print(b)
    print(listem)
    print(dictonarym)

my_function(1,2,3,4,5,key='anahtar',value='deger')