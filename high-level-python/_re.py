

import re


# re module

# re.findall()

str = "python ogreniyorum python"

result = re.findall("python",str) # bize icinde olup oladigini soyler
x = len(result) # kac tane oldugunu verir
print(result)
print(x)

# re.split()

result = re.split(" ",str) # ' ' karakterine gore parcaladi

print(result)

# re.sub()

result = re.sub(" ","-",str) # ' ' yerine - koyar

print(result)

# re.search()

result = re.search("python",str) # python u str de arar yerlerini dondurur

print(result)

# regular expression

result = re.findall("[a-z]",str) # koseli parantez icerdeki karakterleri aratir a dan e 

print(result)

result = re.findall("[^bcdep]",str) # ^ isaret disinda demek

print(result)

result = re.findall("..",str) # .. bize ikili grupları dondurr nokta sayisi belirler

print(result)

result = re.findall("^p",str) # p ile basliyorsa dondurur

print(result)

result = re.findall("n$",str) # n ile bitiyorsa dondurur

print(result)

# daha fazlasi icin python regular expression lara bakabilirsin