import sys

# one string given as input: "1, 2, 3, 4, 5, 5"
mylist = sys.argv[1]
# remove all characters from the strings that are not needed for creaeting the list
mylist = mylist.replace(" ", "")
mylist = mylist.replace("]", "")
mylist = mylist.replace('[', "")
mylist = mylist.replace(',', "")
mylist = mylist.replace('"', "")
mylist = mylist.replace("'", "")

# create a set from the list that will remove the duplicates
myset = set(mylist)
# convert the set to a list and print it out
mylist = list(myset)
print(mylist)

