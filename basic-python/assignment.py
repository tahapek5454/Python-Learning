
from re import X




values = 1 , 2 # kendi tuple tanımladı

x,y = values  # elemanlarını sırayla x ve y  ' ye atadi

print(x,y)


values = 1,2,3,4,5

x,y,*z = values # fazlalık '*' isaretli degiskene liste olarak eklenir

print(x,y,z)
