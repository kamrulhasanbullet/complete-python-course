# Write a python program using function to convert Celsius to Fahrenheit.


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


c = int(input("Enter temperature in Celsius: "))
f = celsius_to_fahrenheit(c)

print(f"{c} degrees Celsius is equal to {round(f, 2)} degrees Fahrenheit.")
