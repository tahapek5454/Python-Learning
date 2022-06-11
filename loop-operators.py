

# for dongusune sayac vermemiz icin range() kullanırız
# range()
for x in range(10):   # x<10 gibi
    print(x,end=" ")
print()
for i in range(2,10):  # i = 2 i<10
    print(i,end=" ")
print()
for x in range(0,10,2): # x=0 x<10 x+=2 
    print(x,end=" ")
print()
# enumerate bize bir stringi karakteri ve indexini dondurur

name = 'taha pek'

for i in enumerate(name):
    print(i)

for index , item in enumerate(name):
    print(f"index = {index} item = {item}")

# zip metodu bize listeleri birlestirir indexlere gore

liste1 = [1,2,3]
liste2 = ['a','b','c']

for i in zip(liste1,liste2):
    print(i)

# yapilabilen islemler

# listelere eleman ekleme yontemleri

numbers = []

for i in range(10):
    numbers.append(i)

print(numbers)

numbers = []

numbers = [x for x in range(10)]

print(numbers)

numbers = []

numbers = [x**2 for x in range(10)]

print(numbers)

numbers = []

numbers = [x**2 for x in range(10) if x%3==0]

print(numbers)

numbers = []

numbers = [x if x%2==0 else 'tek' for x in range(10)]

print(numbers)

numbers = []

numbers = [[x,y]  for x in range(3) for y in range(3)]

print(numbers)
