#  Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.


class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        return f"Vector{self.components}"


# Example usage:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v_sum = v1 + v2
v_dot = v1 * v2
print("Sum of v1 and v2:", v_sum)
print("Dot product of v1 and v2:", v_dot)
