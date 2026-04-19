# Write a python function which converts inches to cms.


def inches_to_cms(inches):
    cms = inches * 2.54
    return cms


inches = int(input("Enter the number of inches: "))
print(f"{inches} inches is equal to {inches_to_cms(inches)} centimeters.")
