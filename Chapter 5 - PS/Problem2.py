# Write a program to input eight numbers from the user and display all the unique numbers (once).

set_of_numbers = set()

number = int(input("Enter a number: "))
set_of_numbers.add(number)
number = int(input("Enter a number: "))
set_of_numbers.add(number)
number = int(input("Enter a number: "))
set_of_numbers.add(number)
number = int(input("Enter a number: "))
set_of_numbers.add(number)
number = int(input("Enter a number: "))
set_of_numbers.add(number)
number = int(input("Enter a number: "))
set_of_numbers.add(number)
number = int(input("Enter a number: "))
set_of_numbers.add(number)
number = int(input("Enter a number: "))
set_of_numbers.add(number)

print("Unique numbers entered:", set_of_numbers)
