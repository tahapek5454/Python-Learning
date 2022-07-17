from tkinter import Y
import pandas as pd
import numpy as np

# data

numbers = [1,2,3,4,5]
letters = ["a","b","c","d",5]
dict = {'a':10 , 'b':20}
rand = np.random.randint(0,11,5)
#Series

# number_s = pd.Series(numbers)


# print(number_s)

# letter_s = pd.Series(letters) # homojen degildir


# print(letter_s)

# s = pd.Series(5,[0,1,2,3])
# print(s)

# number_s = pd.Series(numbers,['a','b','c','d','f'])
# print(number_s)

# print(pd.Series(dict))

# print(pd.Series(rand))

number_s = pd.Series(numbers,['a','b','c','d','f'])

print(number_s)

print(number_s[0])
print(number_s[-2:])
print(number_s['a'])
print(number_s[['a','c']])
print(number_s[['a','c','f']])
print(number_s.ndim) #boyutunu verir
print(number_s.shape) 
print(number_s.sum())
print(number_s.max())
print(number_s.min())
print(number_s + number_s)

print(number_s % 2 == 0)
print(number_s[number_s % 2 == 0])


x = pd.Series([1,2,3],['a','b','c'])
y = pd.Series([4,5,6],['a','b','d'])
r = x+y 
print(r) #karsiligini bulamadigina nan yazar
# serilerin birlesimi dataframdir