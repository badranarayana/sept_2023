"""
"""
"""
What is dictionary?
--> it is one of the key value storage data structure in python
--> we can create dict by using { }
--> we can create using dict() --> {}
--> it is not an sequence object, no index support

--> key should be immutable object and values could be any kind of object


syntax:
------
<var> = {key1: val1, key2:val2, ......}

data = {} # empty dictionary
or 
data = dict() # empty dict

"""
# create dict to store student info
info = {'name': "Sai", 'age': 30, 'roll_number': "Aw003",
        'grade': "10th"
        }
print(type(info))

# get the student name
# dict[key]
print(info['name'])
# get roll_number
print(info['roll_number'])

# adding new values to exiting dict
# dict[key] = val
info['location'] = "HyD"
print(info)
info['blood_group'] = "O+"
print(info)
info['blood_group'] = "B+"

# get blood group
print(info['blood_group'])
print(info)


# delete the key from dict
del info['name']
del info
#print(info)
#---------------------------------------------
# over view
# create dict data
data = {'company_name': "wipro", "location": "hyd"}
# access dict values
data['company_name']

# add new key pair
data['code'] = 'WIPRO1233'

# update exiting key with new value
data['location'] = "BNG"

# delete the data
del data['code']

# delete entire object from memory
del data
#print(data) # should raise not defined error

# --- looping over dictionary
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for i in data:
    print(f"{i} ---> {data[i]}")


