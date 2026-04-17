# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter a username: ")

if len(username) < 10:
    print("The username contains less than 10 characters.")
else:
    print("All is well. The username contains 10 or more characters.")
