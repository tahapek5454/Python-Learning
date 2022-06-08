
# BMW Mercedes Opel Mazda elemanlarına ait bir liste olusturunuz

from unittest import result


arabalar = ["BMW","Mercedes","Opel","Mazda"]

# liste kac elemanlidir

print(len(arabalar))

# listenin ilk ve son elemani

print(arabalar[0])
print(arabalar[-1])

# Mazda degerini toyata ile yer degistirin

# arabalar[-1].replace("Toyata")

arabalar [3] = "Toyata"

print(arabalar)

# mercedes listede bir eleman midir

result = "Mercedes" in arabalar   # kendi bir arama gerçekleştirir

print(result)

# Listenin -2 indexindeki eleman nedir

print(arabalar[-2])

# Listenin ilk 3 elemani nedir

print(arabalar[:3])

# listeye audi ve nissan ekle

arabalar = arabalar + ['audi','nissan']

print(arabalar)

# listenin son elemanını siliniz 

del arabalar[-1]

print(arabalar)

# liste elemanlarını tersten yazdiralim

print(arabalar[::-1])


