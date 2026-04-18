# Attempt problem 1 using while loop.

number = int(input("Enter a number to print its multiplication table: "))

i = 1

while i < 11:
    print(f"{number} x {i} = {number * i}")
    i += 1
