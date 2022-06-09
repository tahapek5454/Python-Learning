
# reference type -> liste 
# C  deki poninter mantığıyla ayni dizilere etki etme

a = ['apple','banana']
b = ['apple','banana']

a = b

a[0] = 'grape'

print(a,b)

# ayni listeyi isaret ettirdigimizden degisiklik ikisine de etki etti
# aslında iki isaretci ayni listeyi gosteriyor