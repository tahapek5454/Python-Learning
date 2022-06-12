
# kendine gonderilen sınırısz parametreyi listeye çeviren fonk tanımla

from gettext import find


def make_list(*params):
    return list(params)

new_list = make_list(1,2,3,4,5,6)

print(new_list)

# gonderilen iki sayi arasındaki tum asal sayilari bulunuz 

def find_prime(a,b):
    prime_list=[]
    flag = True

    for i in range(a,b):
        if i<=1:
            continue
        for j in range(2,i):
            if (i%j == 0):
                flag = False
        if flag:
            prime_list.append(i)
        flag = True
    

    return prime_list


asal_listesi = find_prime(0,12)

print(asal_listesi)

        

                