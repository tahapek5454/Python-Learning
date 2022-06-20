# w (write)

# result = open(r"C:\Users\90543\Desktop\VS\python\manage-folder\newfiles.txt","w",encoding="utf-8")

# result.write("Taha Pek Ülker")

# result.close()

# encoding="utf-8" turkce karakterlein taninmasini sağlar
# r \ en i duzgun formesi icn 
# open fonskiyonu bize verilen dizinde verilen
# komuttan dosya acar ve isaretcisini dondurur


# a (append)

# result = open(r"C:\Users\90543\Desktop\VS\python\manage-folder\newfiles.txt","a",encoding="utf-8")

# result.write(" Şu an ekleme yapiyorum")
# result.write("\nalt satirdayim")

# result.close()
# dosya yoksa acar

# x (create)

# result = open(r"C:\Users\90543\Desktop\VS\python\manage-folder\newfiles2.txt","x",encoding="utf-8")

# birden fazla calistirirsak varsa o dosya hata verir

# r (read)

try:
    file = open(r"C:\Users\90543\Desktop\VS\python\manage-folder\newfiles.txt","r",encoding="utf-8") 
    # eger mod belirtmessem okuma olur
    # print(file)

    # for dongusuyle okuma

    # for i in file:
    #     print(i,end="")

    # content = file.read()
    # print(content) # icerik oldugu gibi okunur
    # bu islemden sonra imlec sondadir tekrardan okuma islemi yaparsan
    # okunacak karakter bulamaz bos donur ""

    # content = file.read(4) # 5 karakter oku

    # print(content)

    # content = file.read(2)
    # print(content)

    # ---------- readline() ise satir satir okutur

    # print(file.readline(),end="")
    # print(file.readline(),end="")


    # ------------ readlines() ise satirlari listeye atar

    # listem = file.readlines()

    # print(listem)



except Exception as ex:
    print("Hata ile karsilasildi")
    print(ex)
finally:
    file.close()

