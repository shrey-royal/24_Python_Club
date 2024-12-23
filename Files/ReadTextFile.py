file_name = input("Enter fileName: ") + ".txt"

with open(file_name, 'r') as file:
    # line = file.read()    # reading file (returns a string)
    # line = file.readline()    # reading single line
    lines = file.readlines()    # reading multiple lines (returns each line in a list)
print(lines, type(lines))