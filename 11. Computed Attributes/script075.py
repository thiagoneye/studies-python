"""
A class named Circle is given.

Add a property to the class called perimeter (read-only) that calculates the length of circle with a given radius.
This property should be computed only at the first reading or after modifying the radius attribute.
To do this, also modify the way of setting the value of the radius attribute in the __init __() method.
Make sure that the value of the perimeter attribute is recalculated when the radius attribute is changed.

Then create an instance named circle with radius=3.

In response, display the value of the perimeter attribute to the console (round the result to four decimal places).
"""

import math

class Circle:
    def __init__(self, radius: int):
        self._radius = radius
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value: 3):
        self._radius = value
        self._area = None
        self._perimeter = None

    @property
    def area(self):
        self._area = round(math.pi * (self._radius**2), 4)
        return self._area
    
    @property
    def perimeter(self):
        self._perimeter = round(2 * math.pi * self._radius, 4)
        return self._perimeter

circle = Circle(3)
print(circle.perimeter)

