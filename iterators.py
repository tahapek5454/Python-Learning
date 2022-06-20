




import re


liste = [1,2,3,4,5,6]


# iterable obke olmasi laizm

# iterator = iter(liste)

# print(next(iterator))

# bu sekilde gezinebiliriz
# for dungusu bize kendi yapiyor bu islemi

# for i in liste:
#     print(i)




# for dongusunde yapilan islem bu

# iterator = iter(liste)

# while True:
#     try:
#         print(next(iterator))
#     except Exception as ex:
#         break

class Numbers:

    def __init__(self,start,finish) -> None:
        
        self.start=start
        self.finish=finish
    
    def __iter__(self):
        return self
    
    def __next__(self):

        if self.start<=self.finish:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration



listem = Numbers(10,20)

for i in listem:
    print(i)



iterator = iter(Numbers(1,3))

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break






