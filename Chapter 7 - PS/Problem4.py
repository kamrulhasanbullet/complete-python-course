# Write a program to find whether a given number is prime or not.

n = int(input("Enter a number to check if it is prime or not: "))

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not a prime number.")
        break
else:
    print(f"{n} is a prime number.")
