"""
File handling is a process to read/write from computer file system

python provides build in function called open() to deal with files reading/writing

# read
# write
# update
"""
# # write program to read and print the content of a file
# file_path = 'data/friends.txt'
# file_obj = open(file_path, 'r')
# print(file_obj)
# print(dir(file_obj))
# content = file_obj.read()
# print(content)
# file_obj.close()

# # write a program to read single line at a time and print
# file_obj = open(file_path, 'r')
# print(file_obj.readline())
# print(file_obj.readline())
# print(file_obj.readline())
# print(file_obj.readline())
# file_obj.close()
#
# # write a program to read all lines at time using readlines()(list of lines)
# file_obj = open(file_path, 'r')
# print(file_obj.readlines())
# print(file_obj.readlines())
# file_obj.close()
#
# # write a program to read the content with specific size
# file_obj = open(file_path, 'r')
# # size
# print("-------------------")
# print(file_obj.read(10))
# print(file_obj.read(10))
# print(file_obj.read(10))
# file_obj.close()
# # readline()
# file_obj = open(file_path, 'r')
# # size
# print("---------------------")
# print(file_obj.readline(30))
# print(file_obj.readline(30))
# file_obj.close()

# write a program to create a file and write some content into that file
# mode 'w' --> write
# create file if file not available
# overwrite the file file available(loss previous saved data)
# file_obj = open('data/colors.txt', 'w')
# file_obj.write("Blue, Red, Yello")
# file_obj.close()
# generally we use write mode('w') when create file and writing content
# we can use 'w' mode if we are ok to lost the previous data)

# write program to write new content to the exiting file with loosing old data
# 'a'

file_obj = open('data/colors.txt', 'a')
file_obj.write("Hyderabad\t")
file_obj.close()

# write a program to write list lines at a time
data = [
    'a,b,c,d\n',
    'e,f,g,h\n',
    'i,j,k,l\n',
    'm,n,o,p\n',
    'q,r,s,t\n',
    'u,v,w,x\n',
    'y,z\n'

]
# file_obj = open('data/alpha.txt', 'w')
# file_obj.writelines(data)
# file_obj.close()

# add numbers alpha.txt without loosing data
file_obj = open('data/alpha.txt', 'a')
file_obj.write('1,2,3,4,5,6,7,8,9,10')
file_obj.close()

# write a program to print the every line length?
# write a code to find how many time 'how' word repeated in given file?
# write a code to find the formers whose age is greater than 40?
