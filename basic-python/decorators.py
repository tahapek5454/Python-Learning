

# def my_decorator(func):

#     def wrapper(name):
#         print("Once")
#         func(name)
#         print("sonra")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("Hello "+name)

# sayHello("ali")

# sayHello()
# sayHello = my_decorator(sayHello)
# print("*"*20)
# sayHello()

# Not : yukardaki atama islemlerini yapmadan da @ kullanrak bu islemi otoamtik yapabilrisn



# ornek biz yapptigimiz islemlerin ne kadar surdugunu ogrenmek isteyebilriz
# her fonksiyona tek tek time calculate ekleyecegimize

import time as t
import math as m

def time_Calculate(func):

    def inner(*parms):
        
        start = t.time()

        t.sleep(1)

        func(*parms)

        finish = t.time()

        print("Gecen Sure {}".format(finish-start))
    return inner

@time_Calculate
def factorial(a):
    print(m.factorial(a))

@time_Calculate
def ust(a,b):
    print(m.pow(a,b))



factorial(10)

ust(2,10)


