

import os

from datetime import datetime


# isletim sistemiyle alakali bilgileri ulasabiliriz...

# result = os.name # isletim sisteminin adi

# result = os.getcwd() # etkin  dosya yolunu verir

# direkt dizini biz de verebiliriz
 
# os.chdir(r"C:\Users\90543\Desktop\VS\python\high-level-python") # .. vererek ust dizine gecis yapariz

# os.mkdir("newdirector") # ayni dizinde dosya olusturur , belirttirigim dizinde olustu

# ic ice klasor olustarabilirz
# os.makedirs("newdirector/yeni")

# rename etme
# os.rename("newdirector","yeniklosur")
# 
# silme
# os.rmdir("newdirector")
# ic ice silme
# os.removedirs("newdirector/newdirector") 

# etkin olan dizindeki klasorleri gormek icin
# result = os.listdir() # parametrede istedigin yolu verebilirsin

# filtreleme islemi

# for i in os.listdir():
#     if i.endswith(".md"):
#         print(i)

# dosyaların biliglerini ulasmak icin

# result = os.stat("README.md")
# dosya boyutuna ulasmak icin
# result = result.st_size # byte cinsinden veriyor

# result = result.st_ctime # bu sekilde anlamsiz bir bilgi veriyor donusum yapacagiz

# olusturulma tarihi
# result = datetime.fromtimestamp(result.st_ctime) # bu sekilde donusum yapiyoruz

# degistirilme tarihi
# result = datetime.fromtimestamp(result.st_mtime)

# os ile istenilen bir dosya calistirilabilir
# os.system("notepad.exe")


#path
# result = os.path.abspath("_os.py") # bize dosyanin tam konumunu verir

# result = os.path.dirname(os.path.abspath("_os.py")) # dizin ismini almis oluruz

# result = os.path.exists("_os.py") # bulundugu dizinde dosyanin olup olmadigini soyler

#result = os.path.isdir(r"C:\Users\90543\Desktop\VS\python\high-level-python") # verilen dizin bir dosya mi

# result = os.path.splitext("_os.py") # uzatiyla osya adini ayirir

# print(result)