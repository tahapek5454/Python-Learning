
name = "taha"
sur_name = 'pek'
age = 18

# str ifadeleri tek tırnak veya cift tırnak arası tanımlayabilirsin

print("adim ve soy adim = "+name+" "+sur_name+" \n my age is = "+str(age))

# index islemler,

print(name[2])

# karakter uzunlugunu len metoduyla buluruz

print(len(name))

# biz eger indexlemede - li ifadelere gecersek sondan eklemeye baslariz

print(name[-1])

# dizideki karakter araligini verebiliriz 1:4 1 dahil 4 dahil degil

print(name[1:4])
print(name[:2]) # bastan basla 2 ye  kadar git
print(name[1:]) # 1 den basla sona kadar git
print(name[:4:2]) # 2 ser 2 ser atalyarak gider