
sets = {'apple','banana','melon'}

 # print(sets[0])   hata sets indexlenemez

 # elemanlara ulasmak icin donguler kullanılır

for x in sets:
    print(x)

sets.add('cheery') # eleman eklemek icin kullanılır

print(sets)

sets.update(['mango','grape']) #toplu ekleme yapmak icin kullanılır

print(sets)

# Not : bir eleman sadece bir kere icerebilir

list = [1,1,1,2,3]

print(list)

print(set(list)) ## listeyi set e cevirdik tekrar edenler gidicek

sets.remove('mango') # mangoyu siler

# sets.discard('mango') ayni islevi gorur

# sets.pop()  indexleme yapmadigindan rastgele bir eleman siler

print(sets)

