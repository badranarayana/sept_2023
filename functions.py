
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


# 13/03/2024
"""

def <func_name>(parameters/arguments):
    .....
    .....
    return


parameters/arguments:
1) required positional args/parameters
2) arbitrary position args(*args)
3) default args
4) arbitrary key ward args(**kwargs)

"""
# example on required positional args


def add(a, b):
    return a + b

out = add(10, 10)
print(out)

def sub(a, b):
    return a - b

out = sub(10, 20)
print(out)


# 2) arbitrary position args(*args)
# can pass unlimited positional args while calling function
# *args will be a tuple object inside function


def dynamic_add(a, b, *args):
    # *args are optional
    # args is available as tuple object
    #print(args)

    total = a + b
    for val in args:
        total += val
    return total

print(dynamic_add(20, 30, 44, 44, 44, 44))


# Write a function to multiply
def mul(x, y, z, *args):
    out = x * y
    for i in args:
        out *= i
    return out

print(mul(20, 3, 4))


def open_account(adhar_card, pan_card, *args):
    if adhar_card and pan_card:
        print("account is activated")
        print("following documents submited")
        print("Adhar ", adhar_card)
        print('pan ', pan_card)
        print("Other documents")
        for doc in args:
            print(doc)
    else:
        print("Required documents missing")

open_account('444', 'dalmldl333', 'driving-3233', 'previos-loan')

# car
def build_car(wheels, engine, breaks, fuel_tank, steering,  *args):
    if wheels and engine and breaks and fuel_tank and steering:
        print("car ready")
        print("with Accessories: ")
        for item in args:
            print(item)

build_car(4, "120cc", "oil breaks", 'petrl', "yes", 'screen', 'floor mat')









