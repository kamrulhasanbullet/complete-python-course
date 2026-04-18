# Write a program to print multiplication table of a given number using for loop.

number = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
