import sys

d={1:'a',2:'b',3:'c',4:'a',5:'d',6:'e',7:'a',8:'b'}
arg = sys.argv[1]
list = []

for x in d:
    if d[x] == arg:
        list.append(x)

print(list)



