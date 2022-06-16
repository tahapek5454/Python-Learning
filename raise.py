

# exception firlatmak icin raise yapisini kullanabilirz

# x = 10

# if x>5:
#     raise Exception("x 5 ten buyuk olamaz")

def checkPassword (my_password):
    import re

    if len(my_password)<3:
        raise Exception("Parola uzunlugu 3 ten kucuk olamaz")
    
    elif not re.search("[A-Z]",my_password):
        raise Exception("Parola Buyuk harf icermelidir")
    
    elif not re.search("[0-9]",my_password):
        raise Exception("Parola rakam icermelidir")
    elif re.search("\s",my_password):
        raise Exception("Parolada bosluk karakteri ' ' bulunmamlidir")
    

psw = "123A456"

try:
    checkPassword(psw)
except Exception as ex:
    print(ex)
else:
    print("Gecerli parola")
