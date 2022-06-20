
from unittest import result


website = "http://www.google.com"

# www den once gelen yerleri siliniz

result = website.lstrip(':/htp')
print(result)

# website degiskenindeki degerde kac tane o harfi var

result = website.count('o')
print(result)

# website icersindeki harfler alfabetik mi

result = website.isalpha()
print(result)

# wbsite icersindeki deger sayi mi

result = website.isdigit()
print(result)