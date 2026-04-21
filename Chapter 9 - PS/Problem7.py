# Write a program to find out the line number where ‘python’ is present from question 6.

with open("log.txt", "r") as file:
    lines = file.readlines()
    line_number = 1
    found = False

    for line in lines:
        if "python" in line:
            print(f"'python' is present in line number: {line_number}")
            found = True
        line_number += 1

    if not found:
        print("'python' is not present in the file.")
