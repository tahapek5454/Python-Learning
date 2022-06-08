



message = "I love python"

print(message)

message = message.upper() #tum karakterleri buyuk harf yapar

print(message)

message = message.lower() # tum karakterleri kucuk harf yapar

print(message)

message = message.title() # her kelimenin bas harfi buyuk yapilir

print(message)

message = message.capitalize() # sadece ilk harf buyuk yapilir

print(message)

message = message.strip() # bosluklari siler

print(message)

message = message.split() #bosluga gore ayirir ve listeye ekler ekstra 'x' x e gore ayir dedeim mesela 

print(message)
print(message[1])

message = ' '.join(message) #araya bosluk ekleyerek listedeki ayrilmis elemanlari birlestirir

print(message)

index = message.find('love') # love i godugu ilk indexi dondurur , yoksa -1 dondurur

print(index)

flag = message.startswith("i") # i harfiyle mi basladigini dondurur

print(flag)

flag = message.endswith("i") # i harfiyle mi bittigini dondurur

print(flag)

message = message.replace('love','like') # love gordugu yere like yazar

print(message)

message = message.replace('love','like').replace(' ','*') # yildiz kurali

print(message)

message = message.center(50) # 50 karakter icersindeki tam ortaya yerlestirir

print(message)

message = "I love python"

message = message.center(50,'-') # 50 karakter icersindeki tam ortaya yerlestirir

print(message)

# you can visit for more info https://www.w3schools.com/python/python_ref_string.asp

