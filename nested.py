

# encapsulation


# def outer(number):
#     print("outer")

#     def inner(number):
#         print("inner")
#         return number+1

#     number2 = inner(number)
    
#     print(number,number2)


# outer(10)




try:
    def factorial(number):

        if not isinstance(number,int): # bu fonksiyon gonderilen degerin o claas a aitligini bildiri
            
            raise TypeError("Please enter to integer")
        
        def inner_factorial(number):

            if(number<=1):
                return 1
            
            return inner_factorial(number-1)*number
        
        return inner_factorial(number)


    print(factorial(5))
except Exception as ex:
    print(ex)
