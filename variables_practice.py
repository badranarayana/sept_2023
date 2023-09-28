Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# variable
# variables are used to store data
# why store data? for future reference
a = 10
# <var_name> = <object>
company_name = "Capgemini"
company_name
'Capgemini'
name
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    name
NameError: name 'name' is not defined
age
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    age
NameError: name 'age' is not defined
age = 27
age
27
age
27
age = 30
age
30
age = 10
age = 30
age = 40
age # ?40
40
# create variable to store number
salary = 30000
# create variable to store location
location = "Hyderabad"
# create variable to store more locations
locations = ['Hyderabad', 'bangalore']
locations
['Hyderabad', 'bangalore']
location
'Hyderabad'
a = 20
b = 30
c = a + b
# 20 + 30 --> 50
a + b
50
# multiple assignment
salary1=salary2=salary3 = 3000
salary1
3000
salary2
3000
salary3
3000
salary1 = 4000
salary2 = 4000
salary3 = 4000
# another approch
age1, age2, age3 = 20, 30, 40
age1
20
age2
30
age3
40
age2, age1, age3 = 20, 30, 40
age2
20
age1
30
age3
40
# c, c++ or compiled programming/static lanaguge
# int a = 30
# char gender = 'M'
# string location = "Hyd"
# pyhon is dynamic datatype lanaguge, variable type will
# decide at run time and not at compile time
a = 30
a = "gggg"
type(a)
<class 'str'>
a = 30
type(a)
<class 'int'>
a = 22.3
type(a)
<class 'float'>
data = []
type(data)
<class 'list'>
type((1,2,3))
<class 'tuple'>
my-var = "John"
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
my_var = "hh"
my var = "hh"
SyntaxError: invalid syntax
