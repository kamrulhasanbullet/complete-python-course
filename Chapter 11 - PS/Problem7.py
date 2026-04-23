# Override the __len__() method on vector of problem 5 to display the dimension of the vector.


class Vector:
    def __init__(self, *args):
        self.values = args

    def __len__(self):
        return len(self.values)

    def __str__(self):
        return f"Vector{self.values}"


v1 = Vector(1, 2, 3)
print(v1)
print(len(f"Vector: {v1}, Dimension: {len(v1)}"))
v2 = Vector(4, 5)
print(f"Vector: {v2}, Dimension: {len(v2)}")
