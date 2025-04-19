"""
A class named Circle is given.

Add a property called area (read-only) to the class that calculates the area of a circle with a given radius.
This property should only be computed at first reading or after modifying the radius attribute.
To do this, also modify the way of setting the value of the radius attribute in the __init __() method.
Make sure that the value of the area attribute is recalculated after changing the radius attribute.

Then create an instance named circle with radius=3.

In response, display the value of the area attribute to the console (round the result to four decimal places).
"""

import math

class Circle:
    def __init__(self, radius: int):
        self._radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value: 3):
        self._radius = value
        self._area = None

    @property
    def area(self):
        self._area = round(math.pi * (self._radius**2), 4)
        return self._area

circle = Circle(3)
print(circle.area)
