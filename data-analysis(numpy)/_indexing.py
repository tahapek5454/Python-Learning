import numpy as np

arr = np.arange(0,50,5)

print(arr)

print(arr[1])
print(arr[1:5])
print(arr[:7])
print(arr[::])
print(arr[::-1])

new_arr = np.array([])

for i in range(len(arr)):
    if i == len(arr)-1:
        break
    new_arr = np.append(new_arr,arr[i])
   

print(new_arr)

multi_arr = new_arr.reshape(3,3)

print(multi_arr)

print(multi_arr[1])

print(multi_arr[1,2])

print(multi_arr[:,2])

print(multi_arr[:,0:2])

print(multi_arr[-1,:])