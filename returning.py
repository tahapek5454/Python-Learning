

def ustalma(number):

    def inner(power):
        return number**power
    
    return inner


two = ustalma(2)

print(two(3))
