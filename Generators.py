"""
Generators in Python:

https://medium.com/edureka/generators-in-python-258f21e3d3ff


What is generator?

--> A Generator in Python is a function that returns
an iterator using the Yield keyword

--> A generator function in Python is defined like a normal function,
    but whenever it needs to generate a value,
    it does so with the yield keyword rather than return.

--> If the body of a def contains yield,
    the function automatically becomes a Python generator function.

When will use generator?
--> we use generator function to write memory efficient programs as
   it generates values on demand(means single value in memory)

Advantages of using generator?
--> used for writing memory efficient programs with less effort as
    it implements __iter__() and __next__() automatically


Syntax:
------
def function_name():
    yield statement

"""

# generate three numbers using yield in function

def genNumber():
    print("Hello World")
    yield 1
    yield 2
    yield 3


def normalfun():
    print("Hello World")
    print("1")
    print("2")
    print("3")
    return "DOne"


out = normalfun()
print(out)

# body won't execute when calling generator function

# generator function returns the generator object and use that object to
# generator the values on demand
# out = genNumber()
# print(out)
#
# print(next(out))
# print(next(out))
# print(next(out))
# print(next(out)) # StopIteration


# Note: next() used to request the values from generator object



# write a generator function to generate 10 numbers

def gen_numbers(n):
    print("Gen started")
    i = 0
    while i <= n:
        yield i
        i = i + 1



gen_object = gen_numbers(5)
print(gen_object)
# print(next(gen_object))
# print(next(gen_object))
# print(next(gen_object))
# print(next(gen_object))
# print(next(gen_object))
# print(next(gen_object))
# print(next(gen_object))

for i in gen_object:
    print(i)



# write generator function for fibanacci series

def fibn():
    first = 0
    second = 1
    while True:
        yield first
        first, second = second, first + second


for i in fibn():
    if i > 50:
        break
    print(i,)



