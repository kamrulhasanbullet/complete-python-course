# Create a Class "Programmer" for storing information of few programmers working at Microsoft.


class Programmer:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language


employee1 = Programmer("Alice", 30, "Python")
employee2 = Programmer("Bob", 25, "Java")
print(
    f"Employee 1: Name: {employee1.name}, Age: {employee1.age}, Language: {employee1.language}"
)
print(
    f"Employee 2: Name: {employee2.name}, Age: {employee2.age}, Language: {employee2.language}"
)
