

listem = ["1","2","5a","10b","abc","50","30"]

# liste elemanlari icindeki sayisal degerleri bulunuz


# for x in listem:
#     try:
#         value = int (x)
#         print(f"sayisal veriler {value}")
#     except Exception as ex:
#         print(ex)


# kullanici q degeri girmedikce girilen her sayinin
# sayi oldugundan emin olunuz

# while  input("Cikis icin q ya devam etmek icin Herhangi bir Tusa basiniz: ")!='q':
#     try:
#         value = int (input("Bir sayi giriniz : "))
#         print("Girilen sayi {}".format(value))
#     except Exception as ex:
#         print(ex)

# parola turkce karakter iceriyorsa bir hata firlatin

turkce_karakterler = "şçğĞüöıİŞÇÜÖ"
parola = "abcçd5"

def checkPassword (psw):
    for x in turkce_karakterler:
        if x in psw:
            raise Exception("Parola turkce karakter icermemeli")

try:
    checkPassword(parola)

except Exception as ex:
    print(ex)
else:
    print("Parola kabul edildi")


    

