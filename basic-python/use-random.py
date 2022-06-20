
import random

value = random.random() # 0.0 - 1.0 arasi

print(value)

value = random.random()*100 # 0.0 - 1.0 arasi

print(value)

# eger tam sayi uretmek ve aralik belirtmek istiyorsam

value = int (random.uniform(5,7))

print(value)

# ya da

x = random.randint(5,7)  # en sagliklisi 5,7 dahil

print(x)


listem = ["taha",'ahmet','mehmet']
# rastgele deger 
print(listem[random.randint(0,len(listem)-1)])

# karakterlerden ve listeden (liste elemanlari da karakter) cekmek icin bir metoda sahip random modulu

print(random.choice(listem))


# 0 dan 10 a kadar sayilari bir listeye atalim

numb =list(range(10))

# bu numb listesini karistiralim

random.shuffle(numb)  # liste elemanlarini karitirmayi sagliyor

print(numb)

# liste icersinden rastgele secilen sayi kadar karakter getirmek iciin

new_liste  = list(range(100))

print(random.sample(new_liste,3))