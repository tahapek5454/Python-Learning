

# with open(r"C:\Users\90543\Desktop\VS\python\manage-folder\newfiles.txt","r+",encoding="utf-8") as file:

#     # r+ demek okuma ve yazma modu demek fakat en bastan iribaren duzenleme yaptirir
#     # seek ile yon belirtmelisin

#     file.seek(5)

#     # 5 ten itibaren artik yazabilirsin


# -------------------------- sayfa sonuna ekleme -------------------------------

# with open(r"C:\Users\90543\Desktop\VS\python\manage-folder\newfiles.txt","a",encoding="utf-8") as file:
#     # artik yazdigim her iceris sayfanin en sonuna gelicek
#     file.write("\n yeni bir bilgi")

# --------------------------- sayfa basina ekleme ----------------------------------

# with open(r"C:\Users\90543\Desktop\VS\python\manage-folder\newfiles.txt","r+",encoding="utf-8") as file:
#     content = file.read()

#     content = "Sayfa basina ekleme\n" + content

#     file.seek(0)
#     file.write(content)

# okuyalim


# --------------------------- sayfa ortasina ekleme ---------------------------------

with open(r"C:\Users\90543\Desktop\VS\python\manage-folder\newfiles.txt","r+",encoding="utf-8") as file:

    listem = file.readlines()
    print(listem)

    listem.insert(1,"listenin 1. indexine writelines kullanarak ekleme \n")

    file.seek(0)

    # for i in listem:
    #     file.write(i)
    
    # for dongusu yerine file.writelines(listem) diyebilirsin

    file.writelines(listem)

   
# with open(r"C:\Users\90543\Desktop\VS\python\manage-folder\newfiles.txt","r",encoding="utf-8") as file:
    
#     print(file.read())