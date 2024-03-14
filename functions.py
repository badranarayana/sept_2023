
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


# 14/03/2024:
"""
Default args:

--> default args are defined with some default value
--> default values will be passed if no value provided
--> it uses provided value if provided, other wise default val will be passed

"""

def salary_hike(current_salary, hike_amount=30):
    return current_salary + hike_amount


print(salary_hike(100, hike_amount=40))
# good per emp
print(salary_hike(100))


def check_scolership(cast='bc'):
    if cast == 'bc':
        print("Eligible for 40%")

    if cast == 'oc':
        print("eligible for 10%")


check_scolership(cast='oc')



def make_car(brand, model, wheel_count=4):
    print("Brand: ", brand)
    print("model ", model)
    print("wheel count ", wheel_count)


make_car('honda', 'amaze')


make_car('honda', 'amaze', wheel_count=6)


# arbitrary kew ward args(**kwargs)
"""
**kwargs : allows us to pass unlimited keyword args while calling function

def <func>(<required args>, *args, var=10, **kwargs):
      pass
      
Kwargs are will be available  as dict object in side function
"""


# student info
def format_student(name, dob, roll_number, school_name="ZPH", **kwargs):
    """

    :param name: ? required positional arg
    :param dob: ? required positional arg
    :param roll_number: ? required positional arg
    :param school_name: keyward/default arg
    :param kwargs: keyword args
    :return:
    """

    #print("KWARGS: ", kwargs)
    student_data = {
        'name': name,
        'dob': dob,
        'roll_number': roll_number,
        'school_name': school_name,
    }

    student_data.update(kwargs)

    return student_data

sai_info = format_student('Sai', '10-03-1994', 'ABC102')
print(sai_info)

badra_info = format_student('Badra',
                            '11-03-1994',
                            'ABC103',
                            school_name="Ravindra",
                            home_address="7-92, hyd",
                            father_name="Punna reddy",
                            city="Guntur"
                            )
print(badra_info)

ramu_info = format_student('ramu',
                            '11-04-1994',
                            'ABC103',
                            school_name="Ravindra",
                            home_address="7-95, hyd",
                            father_name=" reddy",
                            city="Guntur",
                            reference="Ravi kumar sir",
                            fee_amount="30000"
                            )
print(ramu_info)


# lets define function with all arg types:
# order of defining args in python
"""
def <func_name>(<required positional args>, <*args>, <default/key word args>, <**kwargs>):
    pass


"""


def example(a, b, *args, location='Hyd', state="TG", **kwargs):
    print("Required args ", a, b)
    print("*args ", args)  # tuple
    print("default/kewword args ", location, state)
    print("**kwargs ", kwargs)  # dict

print("--------------------------")

example(10, 20, 30, 40, mobile_number="5513333", name='Sai', location="GUNTUR")











