'''

# more example:
https://github.com/badranarayana/Python_2021/blob/main/comprehensions.py
What is Comprehensions in Python?
comprehensions in python provides a
short and concise way to create new sequence
from existing sequence object

python provides 4 types of comprehensions
1) List comprehension
2) dict comprehension
3) set comprehension
4) generator/tuple comprehension
'''
# List comprehension:
# list comprehension create a new list from existing iterable object
"""
syntax:
------- 
           1              2                3
data = [expression for item in items <if condition>]      

execution order: 2 -->  3 (True) --> 1(output)     
"""

# classic way
items = ['a', 'b', 'c', 'd']
data = []
for char in items:
    upper_char = char.upper()
    data.append(upper_char)
print(data)

# using comprehension
output = [item.upper() for item in items]
print(output)


# write a program to filter whose name start with 's'?

names = ['badra', 'sai', 'ravi', 'somesh']

output = [name.upper() for name in names if name.startswith('r')]
print(output)

# write a program to find even numbers using list comprehensions:
data = [2, 5, 6, 8, 9, 12, 16]
# list of even numbers
out = [num for num in data if num % 2 == 0]
print(out)
# odd numbers
out = [num for num in data if num % 2 != 0]
print(out)

# classic way
even_list = []
odd_list = []
for num in data:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print(even_list, odd_list)

# dict comprehension:
# dict comprehension create new dict from existing iterable object
"""
syntax:
------
data = {<expression> <for loop> <condition> }
"""
data = [('name', 'Sai'), ('age', 30), ('location', "hyd")]
out = {item[0]: item[1] for item in data} # dict
print(out)


# set comprehension
out = {item[0] for item in data}  # set object
print(out)

# write program to demonstrate set comprehension
# set allows us to remove duplicate and only keep unique values

data = [1, 30, 2, 3, 4, 2, 4, 5]
out = {i for i in data}
print(out)

# create set
data = {1, 30, 5, 2, 4, 3, 4,30,222, 5, 4, 6, 9}
print("&&&&", data)


# write a program to remove duplicate and sort in ascending order

data = [1, 2, 3, 1, 4, 33, 2, 99, 3, 100, 10, 99, 100]
out = set(data)  # won't order by
print(out)

data = {i for i in sorted({i for i in data})}  # returns list
print(data)


# nested loops in comprehensions:
data = [(1, 2, 3, 4), [3, 4, 5, 6], (4, 22, 44, 55), (1, 2)]
# output: flat the above list like below
# [1, 2, 3, 4, 3, 4, 5, 6,4,22,44,55,1,2]
# classic
out = []
for item in data:
    for i in item:
        out.append(i)
print(out)

# comprehension
out = [i for item in data for i in item if i > 4]
print(out)

