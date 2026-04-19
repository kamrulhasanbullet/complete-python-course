# Write a recursive function to calculate the sum of first n natural numbers.


def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)


# Example usage:
number = 10
result = sum_of_natural_numbers(number)
print(f"The sum of the first {number } natural numbers is: {result}")
