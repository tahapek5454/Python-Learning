
import numpy as np

array = np.array([1,2,3,4,5])

print(array)

array = np.arange(0,11)

print(array)

array = np.arange(0,10,3)

print(array)

array = np.zeros(10)

print(array)

array = np.ones(10)

print(array)

# verdigimiz baslangic ve biris degerini esit araliklarla boler

array = np.linspace(0,100,5)

print(array)

array = np.random.randint(0,20)

print(array)

np_array = np.arange(50)
multi_array = np_array.reshape(5,10)
print(multi_array)
# satirlarin ve stunlarin toplami
print(multi_array.sum(axis=1))
print(multi_array.sum(axis=0))

rnd_array = np.random.randint(0,100,5)
print(rnd_array)
print(rnd_array.max())
print(rnd_array.argmax())
print(rnd_array.min())
print(rnd_array.argmin())