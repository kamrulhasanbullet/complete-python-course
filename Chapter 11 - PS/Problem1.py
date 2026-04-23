# Create a class (2-D vector) and use it to create another class representing a 3-D vector.


class vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __show__(self):
        print(f"The 2D vector is: {self.x}x + {self.y}y")


class vector3D(vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __show__(self):
        print(f"The 3D vector is: {self.x}x + {self.y}y + {self.z}z")


a = vector2D(2, 3)
a.__show__()
b = vector3D(5, 3, 4)
b.__show__()
