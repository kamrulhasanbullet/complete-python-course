# Write a program to find the greatest of four numbers entered by the user.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

# first way to find the greatest number using if-elif statements
greatest = num1
if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
if num4 > greatest:
    greatest = num4


# second way to find the greatest number using the built-in max() function
# greatest = max(num1, num2, num3, num4)


# third way to find the greatest number using nested if-else statements
"""if num1 > num2 and num1 > num3 and num1 > num4:
    greatest = num1
elif num2 > num1 and num2 > num3 and num2 > num4:
    greatest = num2
elif num3 > num1 and num3 > num2 and num3 > num4:
    greatest = num3
else:
    greatest = num4"""


print("The greatest number is:", greatest)
