import sys

# string from cli argument
arg_str = sys.argv[1]
dict = {}

# go through each element in the string and if the element exists: +1 if not set to 1
for i in arg_str.lower():  # to lower case according to the example in moodle
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

# print result
print(dict)