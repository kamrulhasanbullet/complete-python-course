# Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not present, a message without exiting the program must be printed prompting the same.

try:
    with open("1.txt", "r") as file1:
        print(file1.read())
except Exception as e1:
    print(e1)

try:
    with open("2.txt", "r") as file2:
        print(file2.read())
except Exception as e2:
    print(e2)

try:
    with open("3.txt", "r") as file3:
        print(file3.read())
except Exception as e3:
    print(e3)
