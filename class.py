

class person:

    name=""
    age=0

    # constructor
    def __init__(this,name="",age=-1): # bizim contrutorımız  # default atama
        this.name = name
        this.age = age
    
    
    
    # instance methods

    def sayHello(this):   # bos bırakamzsın self ya da this koyacaksın metoda ait
        print("hello")
    
    def calculateYear(this):
        return 2022-this.age
    

p1 = person('taha',19)
p2 = person("Ahmet",20)

print('name : {} age : {}'.format(p1.name,p1.age))
print('name : {} age : {}'.format(p2.name,p2.age))

p1.name='tarik'
print('name : {} age : {}'.format(p1.name,p1.age))

p1.sayHello()

print(f"dogum yilim = {p1.calculateYear()}")

p3 = person()

print(f"p3 un adi {p3.name} ve yasi {p3.age}")