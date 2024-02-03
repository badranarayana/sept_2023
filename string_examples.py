name = "Badra"
age = 30
name = badra
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'badra' is not defined
a = 10
b = a
b
10
a
10
b = c
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'c' is not defined
b = 'c'
#  built in methods
# len()
len("hello")
5
len("w")
1
len(' ')
1
# note: space also an charector in python
len("Hello world")
11
# dir --> used to list out all attributes from given object
dir('')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# convert the given string to upper case
name = 'sai' # 'SAI'
name.upper()
'SAI'
name
'sai'
# covert given string into lower case
data = "HYDraBAD"
data.lower()
'hydrabad'
data
'HYDraBAD'
# covert the given string into title case
company_name = "wipro pvt ltd"
company_name.title()
'Wipro Pvt Ltd'
name = 'sai reddy'
name.title()
'Sai Reddy'
name = "SAI reddy"
name.title()
'Sai Reddy'
name = 'sai reddy'
name.capitalize()
'Sai reddy'
name = "SAI REDDY"
name.capitalize()
'Sai reddy'
help("".center)
Help on built-in function center:
center(width, fillchar=' ', /) method of builtins.str instance
    Return a centered string of length width.
    
    Padding is done using the specified fill character (default is a space).
name = "sai kumar reddy"
name
'sai kumar reddy'
name.count('a')
2
name.count("r")
2
name.count(" r")
1
name.count('Sai')
0
# case sensitive
name.count('sai')
1
name
'sai kumar reddy'
# check give string starts with "mu" or not
name = 'muthyam priya'
name.startswith("mu")
True
name.startswith("ut")
False
name.startswith("mut")
True
name.startswith("priya")
False
# check give string ends with 'reddy' or not
name = 'ramana rao'
name.endswith('reddy')
False
name = "Sai reddy"
name.endswith("reddy")
True
name.endswith("y")
True
name
'Sai reddy'
name.endswith('ddy')
True
# check give file is pdf or not?
file_name = "numbers.txt"
file_name.endswith(".pdf")
False
file_name.endswith(".txt")
True
file_name2 = "photos.pdf"
file_name.endswith(".pdf")
False
file_name2.endswith(".pdf")
True
file_name3 = "locations.PdF"
file_name3.endswith(".pdf")
False
file_name3.lower().endswith(".pdf")
True
file_name3 = "locations.PDF"
file_name3.lower().endswith(".pdf")
True
# find the index of give char
data = "abcdxyz"
data.index('x')
4
data.index('xy')
4
data.index("bcd")
1
data = "abcabc"
data.index("a")
0
data.index("c")
2
# find the all index of 'c'
data
'abcabc'
# enumerate() used to deal with index and value
data
'abcabc'
enumerate(data)
<enumerate object at 0x0450F328>
list(enumerate(data))
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'a'), (4, 'b'), (5, 'c')]
for index, value in enumerate(data):
...     if value == 'c':
...         print(index)
... 
2
5
# check give string contains only digits or not
data = "12334"
data.isdigit()
True
data1 = "abc123"
data1.isdigit()
False
data = ' '
data.isspace()
True
data1 = ' 2'
data1.isspace()
False
data = '1233'
data.isnumeric()
True
data1 = '1233wee'
data1.isnumeric()
False
help("".isdigit)
Help on built-in function isdigit:
isdigit() method of builtins.str instance
    Return True if the string is a digit string, False otherwise.
    
    A string is a digit string if all characters in the string are digits and there
    is at least one character in the string.
"1".isdigit()
True
"".isdigit()
False
help("".isnumeric)
Help on built-in function isnumeric:
isnumeric() method of builtins.str instance
    Return True if the string is a numeric string, False otherwise.
    
    A string is numeric if all characters in the string are numeric and there is at
    least one character in the string.
"22.3".isdigit()
False
"22.3".isnumeric()
False
"22a".isnumeric()
False
"22a".isdigit()
False
# strip
" hello ".strip()
'hello'
data = "hello "
data.rstrip()
'hello'
data = " hello "
data.rstrip()
' hello'
data.lstrip()
'hello '
data.lstrip().rstrip()
'hello'
data
' hello '
data.strip()
'hello'
# replace .txt with .pdf
file_names = "file.txt,file2.txt,file3.txt"
file_names.replace(".txt", '.pdf')
'file.pdf,file2.pdf,file3.pdf'
file_names
'file.txt,file2.txt,file3.txt'
name = 'satya rao'
name.replace("rao", "reddy")
'satya reddy'
name
'satya rao'
name = "Sai muthyam"
name.replace('th', 't')
'Sai mutyam'
# split 
name = "sai muthyam"
# first_name
# last_name
name.split()
['sai', 'muthyam']
out = name.split()
out
['sai', 'muthyam']
first_name = out[0]
last_name = out[1]
first_name
'sai'
last_name
'muthyam'
record = "sai|10-03-1994|hyderabad|500072"
details = record.split("|")
details
['sai', '10-03-1994', 'hyderabad', '500072']
name = details[0]
dob = details[1]
location= details[2]
pin = details[3]
name
'sai'
dob
'10-03-1994'
location
'hyderabad'
pin
'500072'
