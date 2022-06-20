
# kaliti miras alma islemi

class Person():

    def __init__(self,name,age) -> None:

        self.name = name
        self.age = age
        print("Person class i")
    
    def eating(this):
        print("eating")

    def ben_kimim(this):
        print("person")

class Student(Person):   # persondan ecxrends edildigi anlasiliyor

    def __init__(self,name,age):
        super().__init__(name,age)   # bu bize Kalitimdaki constructor ı da baslatir
        # super kullanmazsan person lı yaparasan self parametresi de gondermlisin
        print("Studen calss i ")
    
    # methods overriding
    def ben_kimim(this):
        print("ben student")
    
p1 = Person("person",10)
s1 = Student('Taha',20)

print(s1.age)
print(s1.name)

p1.eating()
s1.eating()
p1.ben_kimim()
s1.ben_kimim()
