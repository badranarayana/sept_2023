
# Functions in python
# What is function?
"""
Function is a reusable block of code with some name

--> allows us pass parameters and return output

"""
# how many type of function there in python
"""
Built-in functions
 example: max(), len(), dir(), min() sorted()...
 
user defined functions:
---------------------
These functions is going define by developers for re usability

 there are two types of functions
 1) def function
 2) lambda function

"""
# Examples on built-in
# data = [1, 2, 3, 4]
# out = len(data)
# print(out)
#
# sai = 'dddd'
# out = len(sai)
# print(out)
#
# # max
# data = (1, 2, 3, 4, 10, 5, 6)
# out = max(data)
# print(out)


# User defined functions
"""
Def function/normal functions

Syntax:
------
def <function_name>(parameters/arguments):
    .....
    .....
    .....
    return output

Note: parameters are optional.
return also optional and return None as default
"""

# 1. Defining function


def print_name(name):
    print(name.upper())
    return "YYYYY"

# 2. calling/invoking function
# func_name(params)
out = print_name('sai')
print(out)
#print_name('badra')
#print_name('ravi')

# write function to find given number is even number or not
def find_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(find_even(4))
print(find_even(33))
print(find_even(44))

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(f"{i} --> {find_even(i)}")

# write a program to find the name in the given list

data = ['sai', 'ravi', 'sam']

def is_exist(items, filter_item):
    return filter_item in items


print(is_exist(data, 'Aam'))








