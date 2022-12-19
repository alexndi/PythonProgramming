import sys

# Get the file name from the command line arguments
file_name = sys.argv[1]

# Open the file in read mode
with open(file_name, 'r') as f:
    # Read the contents of the file into a list
    lines = f.readlines()

# Sort the list of lines
sorted_lines = sorted(lines)

# Open the file in write mode
with open(file_name, 'w') as f:
    # Write the sorted lines to the file
    f.writelines(sorted_lines)

# Close the file
f.close()