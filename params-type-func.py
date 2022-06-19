

def toplama(a,b):
    print(a+b)

def cikarma(a,b):
    print(a-b)

def islem(f1,f2,type):
    
    if type=="toplama":

        f1(5,2)

    elif type=="cikarma":
        f2(7,1)

islem(toplama,cikarma,"toplama")

islem(toplama,cikarma,"cikarma")
    
