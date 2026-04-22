# Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = 0. Does this change the class attribute?


class MyClass:
    a = 10  # Class attribute


# Create an object of MyClass
obj = MyClass()
# Set 'a' directly using the object
obj.a = 0
# Check the value of 'a' in the object and the class
print("Value of a in object:", obj.a)  # This will print 0

print(
    "Value of a in class:", MyClass.a
)  # This will still print 10, as the class attribute is unchanged

