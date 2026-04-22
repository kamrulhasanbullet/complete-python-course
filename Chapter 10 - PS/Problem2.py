# Write a class "calculator" capable of finding square, cube and square root of a number.


class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The square of {self.number} is {self.number ** 2}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number ** 3}")

    def square_root(self):
        print(f"The square root of {self.number} is {self.number ** 0.5}")


Calculator(5).square()
Calculator(5).cube()
Calculator(5).square_root()
