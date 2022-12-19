import sys

# take arguments from cli
test_list = sys.argv[1:len(sys.argv)]

flag = 0

# checks if the list is sorted
if(test_list == sorted(test_list)):
    flag = 1

# print according to flag if the list is sorted
if (flag) :
    print ("sorted")
else :
    print ("unsorted")
