"""
An implementation of the Vector class is given.

Implement the __bool__() special method to return the logical value of vector:
- False in case the first coordinate is zero
- on the contrary True

If the user doesn't pass any argument, return the logical value False.
"""

class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __bool__(self):
        if not self.components:
            return False
        return bool(self.components[0])

v1 = Vector()
v2 = Vector(3, 2)
v3 = Vector(0, -3, 2)
v4 = Vector(5, 0, -1)
 
print(bool(v1))
print(bool(v2))
print(bool(v3))
print(bool(v4))
