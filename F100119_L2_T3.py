import sys

# one string given as input: "1, 2, 3, 4, 5, 5"
mylist = sys.argv[1]
# find the length of the list

mylist = mylist.replace(" ", "")
mylist = mylist.replace("]", "")
mylist = mylist.replace('[', "")
mylist = mylist.replace(',', "")
mylist = mylist.replace('"', "")
# create a set from the list that will remove the duplicates
myset = set(mylist)

print(myset)
# compare the length of the list and set and print if the list contains duplicates
if len(mylist) != len(myset):
    print("True")
else:
    print("False")
