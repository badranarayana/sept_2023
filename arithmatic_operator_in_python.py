Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# operator nothing but a symbol used to perform opertion on values
# create variable (=)
a = 30
30 + 40
70
3- = 40
SyntaxError: invalid syntax
30 - 40
-10
# + operator
# addition
num1 = 30
num2 = 40
num1 + num2
70
# here + is operator, num1 left operand and num2 right operand
50 + 44
94
# using + between numbers
20 + 30 # valid? True
50
44 + 44.5 # valid
88.5
44.5 + 44 # valud??True
88.5
# using + between string and int
"Hello" + 33
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    "Hello" + 33
TypeError: can only concatenate str (not "int") to str
"hello" + "Hi"
'helloHi'
# - operator
# substraction
40 - 55
-15
44.5 - 55.7
-11.200000000000003
# - between str and number
"44" - 44 #invalid
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    "44" - 44 #invalid
TypeError: unsupported operand type(s) for -: 'str' and 'int'
"44" - "55"
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    "44" - "55"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
# * multipication
salary = 300
# give 2 times hike on existing salary
new_salary = salary *  2
new_salary
600
# using * on int and float
40 * 33.7
1348.0
# using * on str and int
'A' * 2
'AA'
'A' * 3
'AAA'
'badra' * 2
'badrabadra'
# repeatition
"Hello" * 1
'Hello'
"Hello" * 3
'HelloHelloHello'
# **
2 ** 2
4
2 ** 6
64
"S" ** 3
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    "S" ** 3
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
party_amount = 3000
members = 4
per_head = party_amount / members
per_head
750.0
per_head * members
3000.0
a = 20
b = 5
a / b # What data type it will return?
4.0
out = a /b
out
4.0
type(out)
<class 'float'>
10//5
2
# floor division
20/5
4.0
20//5
4
type(20//5)
<class 'int'>
type(20/5)
<class 'float'>
type(3)
<class 'int'>
# % module
# write a program to check given number is even or not
num = 10
# even? Yes
num % 2
0
num = 9
num % 2
1
num = 6
num % 2
0
# home work
# write a program to find out the total amount after 100 discount
# shirt_price = 4000
# dicount = 100
# total = ?


# write a program to find the GST of 10% on total bill
# bill_payment = total + GST amount
