numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

val = min(numbers) # numbersdaki min degeri dondurur

print(val)

val = max(numbers) # numbersdaki max degeri dondurur

print(val)

val = max(letters)

print(val)

val = min(letters)

print(val)

numbers.append(20) # 20 elmanini ekledik

print(numbers)

numbers.insert(2,89) # belirtilen index e elaman ekler eklendiği yerdeki elemani saga kaydirir

print(numbers)

numbers.pop() ## sondaki elemani siler

print(numbers)

numbers.pop(2) ## index numarasi verilen elemani siler

print(numbers)

numbers.remove(16) ##silmek istedigimiz degeri direkt belirtmek icin kullanilir

print(numbers)

numbers.sort() # numbers i siralar

print(numbers)

numbers.reverse() # ters cevirmemizi saglar

print(numbers)

numbers.clear() # tum elemanlari siler

print(numbers)