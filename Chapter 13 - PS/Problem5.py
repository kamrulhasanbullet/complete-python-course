# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce


def greater(a, b):
    if a > b:
        return a
    return b


list = [545, 54, 88, 99, 54564, 55555]

print(reduce(greater, list))
