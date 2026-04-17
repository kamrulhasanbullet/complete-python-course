# Write a program which finds out whether a given name is present in a list or not.

list_of_names = ["Alice", "Bob", "Charlie", "David", "Eve"]

name_to_find = input("Enter a name to find: ")

if name_to_find in list_of_names:
    print(f"{name_to_find} is present in the list.")
else:
    print(f"{name_to_find} is not present in the list.")
