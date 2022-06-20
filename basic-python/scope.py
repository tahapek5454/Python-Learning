
# bir global sabit degiskenin degerini fonksiyonda degistirmek istersek
# fonksiyonun icersinde o degiskenin adini aynı bir sekilde global etiketiyle tanımlamalıyız
# aksi taktirde isler kendi scopuna ozgu olmaya devam eder

sayi = 50

def change_Sayi(value):
    global sayi

    print("sayini degismeden onceki degeri {}".format(sayi))

    sayi = value

    print("sayinin yeni degeri {}".format(sayi))

change_Sayi(100)
print("*"*100)
print(sayi)

## direkt adresine ulasip islemleri gerceklestirdik referanslı islem yaptik