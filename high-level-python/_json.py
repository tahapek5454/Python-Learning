
import json

# dict modeli gibi

person = {"name" : "taha", "languages" : ["python","c"]}

print(person["name"])

print(person["languages"])

print("*"*20)

# bu modeli string e donusturune json model olur

person_string = '{"name" : "taha", "languages" : ["python","c"]}' # json model

# Json strig to dict

result = json.loads(person_string) # cevirme islemini yapar

print(type(result))

print(result)
print("*"*20)
# dosyadan okuma

# with open(r"C:\Users\90543\Desktop\VS\python\high-level-python\person.json") as f:
#     data = json.load(f)
#     print(data)

print("*"*20)

# Dict to Json

person_dict = {"name" : "taha", "languages" : ["python","c"]}

result = json.dumps(person_dict) # dict to json

print(type(result))

# dosyaya yazdirma islemi

# with open(r"C:\Users\90543\Desktop\VS\python\high-level-python\person.json","w") as f:

#     print(type(person_dict))
#     json.dump(person_dict,f)
#     print("eklendi")


# okunurlugu arttirabilmek icin

result = json.dumps(person_dict,indent=4, sort_keys=True) # okunurlugu artirir

print(result)
print("-"*50)
print(person_dict)
