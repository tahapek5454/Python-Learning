

from asyncore import read


with open(r"C:\Users\90543\Desktop\VS\python\manage-folder\newfiles3.txt","r",encoding="utf-8") as file:

    print(file.tell())

    content = file.read()

    print(content)

    print(file.tell())

    file.seek(1)

    print(file.tell())

    content2 = file.read()

    print(content2)

    print(file.tell())

# bu islem otomatik bloktan cikinca closelanmasini sagliyor