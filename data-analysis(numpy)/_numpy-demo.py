import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.

dizi = np.array([10,15,30,45,60])
print(dizi)
print("*"*50)
# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.

dizi = np.arange(5,15)
print(dizi)
print("*"*50)
# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.

dizi = np.arange(50,100,5)
print(dizi)
print("*"*50)
# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.

dizi = np.zeros(10)
print(dizi)
print("*"*50)
# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.

dizi = np.ones(10)
print(dizi)
print("*"*50)
# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.

dizi = np.linspace(0,100,5)
print(dizi)
print("*"*50)
# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.

dizi = np.random.randint(10,30,5)
print(dizi)
print("*"*50)
# 8- [-1 ile 1] arasında 10 adet sayı üretin.

dizi = np.random.randn(10)
print(dizi)
print("*"*50)
# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.

dizi = np.random.randint(10,50,15)
dizi = dizi.reshape(3,5)
print(dizi)
print("*"*50)
# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız ?

print(dizi.sum(axis=1))
print(dizi.sum(axis=0))
print("*"*50)
# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?

print(dizi.max())
print(dizi.min())
print(dizi.mean())
print("*"*50)
# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır ?

print(dizi.argmax())
print("*"*50)
# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

dizi = np.arange(10,20)
print(dizi[0:3])
print("*"*50)
# 14- Üretilen dizinin elemanlarını tersten yazdırın.

print(dizi[::-1])
print("*"*50)
# 15- Üretilen matrisin ilk satırını seçiniz.

dizi = np.random.randint(10,50,15)
dizi = dizi.reshape(3,5)
print(dizi)
print(dizi[0])
print("*"*50)
# 16- Üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir ?

print(dizi[1][2])
print("*"*50)
# 17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.

print(dizi[:,0])
print("*"*50)
# 18- Üretilen matrisin her bir elemanının karesini alınız.

print(dizi[:,:]*dizi[:,:])
print("*"*50)
# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ?

print(dizi[dizi % 2 == 0])
print("*"*50)