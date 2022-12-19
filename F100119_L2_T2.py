import sys

# take 2 arguments from cli
string_1 = sys.argv[1]
string_2 = sys.argv[2]

# convert them into lowercase
string_1 = string_1.lower()
string_2 = string_2.lower()

# check if the length of the strings are the same
if(len(string_1) == len(string_2)):

    # sort the strings
    sorted_string_1 = sorted(string_1)
    sorted_string_2 = sorted(string_2)

    if sorted_string_1 == sorted_string_2:
        print("True")
    else:
        print("False")

else:
    print("False")
