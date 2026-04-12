# Write a python program to print the contents of directory using the os module.
# Search online for the function which does that
# Label the program written in problem 4 with comments

import os

# get current directory path
path = os.getcwd()

# get list of files and directories
contents = os.listdir("/")

# print contents
print("Directory contents:")
for item in contents:
    print(item)
