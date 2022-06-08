
name = 'taha'
sur_name = 'pek'
age = 18

print("my name is {}".format(name)) ##bu islem string icersine format kullanarak deger eklemeye yarar

print("my name is {} {}".format(name,sur_name)) ##bu islem string icersine format kullanarak deger eklemeye yarar

print("my name is {1} {0}".format(name,sur_name)) ##bu islem string icersine format kullanarak deger eklemeye yarar

print("my name is {s} {n}".format(n=name,s=sur_name)) ##bu islem string icersine format kullanarak deger eklemeye yarar

## bu formatlama islminde tur donusumune gerek kalmaz

print("my name is {} {} my age : {}".format(name,sur_name,age)) ##bu islem string icersine format kullanarak deger eklemeye yarar

result = 200/700

print(result)

print("result = {}".format(result))

print("sade result : {r:1.2}".format(r=result))  # bu yazım sekli virgülden sonra kac basamak olacıagını ve virgülden once bolsuk oluğ
                                                # olmayacagini belirtir
# bir diger yontem

print(f"my name is {name} {sur_name} my age : {age}") # f parametresi ekleyerek basitce gerceklestirilebilir
