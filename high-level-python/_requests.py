
# You shoul instaal requests modul
# pip install --user requests

# internet saydalarindaki kaynak kodlarına ulasbiliyoruz
# web sitesine bir talebin python araciligyla yapilmasidir
import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")

result = result.text # adres uzerinden gelen json bilgileri aliriz

# veriler bize string yapida geliyor

print(result)

print(type(result))

# biz bu verileri json stringten dict e cevirebilirz

dict = json.loads(result)

print(dict[0]["id"])
print(dict[0])

print(type(dict))

# toplu duzenli cekim

for i in dict:
    print(i)

