# Write a program to filter a list of numbers which are divisible by 5.


def divisibleBy5(n):
    if n % 5 == 0:
        return True
    return False


numbers = [555, 55, 155, 77, 50, 79]
result = list(filter(divisibleBy5, numbers))

print(result)
