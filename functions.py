
# tanımla def ile yapılır ve eger degiskene deger atarsak bos geldiginde
# o degiskenin yerine atama yaptigimiz islem gecer
def sayHello(name = 'user'):
    print("hello "+name)

sayHello()
sayHello('taha')

# bu sekilde deger dondurebiliriz
# alttaki islemde fonksiyonun açıklaması olur
def sayHello2(name = 'user'):
    '''
    DOCSTRING : Bu fonksiyon merhaba der
    INPUT : parametre isim alir
    OUTPUT : MERHABA USER
    '''

    return "hello "+name

msg = sayHello2()
print(msg)
print(help(sayHello2))