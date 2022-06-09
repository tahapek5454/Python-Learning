
x = 5

flag = x > 1 and x<10  ## and operatoru direkt and diye yazılır

print(flag)

flag = x > 10 or (x%5==0)  ## or operatoru direkt or diye yazılır

print(flag)

# ! yerini python da not a bırakır


x = y = [1,2,3]
z = [1,2,3]

flag = x==y
flag2 = x==z     # alısılagelmişten farklı burdaki esittir isareti direkt degerler uzerinden esitlik bakar
print(flag)
print(flag2)


flag = x is y
flag2 =  x is z    # referans esitligini 'is'  komutuyla kontrol edersin

print(flag)
print(flag2)

print(1 in x) # burda da 1 x ' in icinde mi degil mi kontorlunu yapıyoruz 'in' komutuyla

