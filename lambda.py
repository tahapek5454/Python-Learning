
def square (numbers):
    return numbers**2

# eger ben bir listenin karesinin alınmasını istersem map metodunu kullanmalıyım
# map metodu liste icersinde gezinip ilgili islemi her veri icin yapar

listem = [1,2,3,4,5]
result = list(map(square,listem))
print(result)

# fonksiyon tanımlamak yerine yapılacak islemi lambda ile tanımlayabilirz

listem = [1,2,3,4,5]
result = list(map(lambda x : x**2 , listem))
print(result)

# lambda kullanarak basit fonksiyonlar da olusutarabiliz

square2 = lambda x : x**2

listem = [1,2,3,4,5]
result = list(map(square2,listem))
print(result)

# filter bize filtreleme islemi yapar dogru veya yanlıs dondurur

def check_even(number): return number%2==0

result = list(filter(check_even,listem))
print(result)

result = list(filter(lambda x : x%2==0 ,listem))
print(result)

check_even2  = lambda x : x%2==0

result = list(filter(check_even2,listem))
print(result)



