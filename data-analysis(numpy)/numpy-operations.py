
import numpy as np

numbers1 = np.random.randint(0,100,6)
numbers2 = np.random.randint(0,100,6)

print(numbers1)
print(numbers2)

result = numbers1+numbers2
result = numbers1-numbers2
result = numbers1-10
result = numbers1*numbers2
#result = numbers1/numbers2
result = np.log(numbers1)
result = np.sin(numbers1)
result = np.sqrt(numbers1)

# matris birlestirme

multi_numbers1 = numbers1.reshape(2,3)
multi_numbers2 = numbers2.reshape(2,3)

print(multi_numbers1)
print(multi_numbers2)

print("*"*50)

# ust uste birlestirir
result = np.vstack((multi_numbers1,multi_numbers2))
# yatay olarak birlestirir
result = np.hstack((multi_numbers1,multi_numbers2))

result = numbers1 > 50
print(numbers1[result])

print(result)