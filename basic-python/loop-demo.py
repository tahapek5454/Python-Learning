
# 1-100 arası gelen sayıları assagi yukarı diye yonlendirerek tahmin ettirmeye calisin

import random

sayi = int(input("Tahmin edilmesini istediginiz sayiyi giriniz : "))

min ,max = 1, 101 
tahmin = random.randint(min,max)


while True:

    print(f"tahmin edilen sayi {tahmin}")

    if sayi == tahmin:
       
        print("Sayi bulundu")
        break
    else:
        if tahmin>sayi:
            max = tahmin
            tahmin = random.randint(min,max)
        elif tahmin<sayi:
            min = tahmin+1
            tahmin = random.randint(min,max)


    











