
# error handling

# try:
#     x = int(input("lutfen bir sayi giriniz : "))
#     y = int(input("lutfen bir sayi giriniz : "))
#     print(x/y)

# except ZeroDivisionError:
#     print("0 a bolum olmaz")
# except ValueError:
#     print("Sayi girmelisiniz")


# bu sekilde de bize hatanin ne oldugunu direkt bildirenbilir


# else kısımı hata almazsan calisir
while True:
    try:
        x = int(input("lutfen bir sayi giriniz : "))
        y = int(input("lutfen bir sayi giriniz : "))
        print(x/y)
    except (ZeroDivisionError,ValueError) as e:
        print("Bir hatayla karsilasildi")
        print(e)
    else:
        print("Her sey yolunda")
        break
    finally:
        print("Finally her zaman calisir")



# bu da hepsini kapsayan sekli
# try:
#     x = int(input("lutfen bir sayi giriniz : "))
#     y = int(input("lutfen bir sayi giriniz : "))
#     print(x/y)
# except Exception as e:
#     print("Bir hatayla karsilasildi")
#      print(ex)
    