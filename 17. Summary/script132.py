"""
The following Point class is given.

Implement the calc_distance() method that calculates the euclidean distance of two points.

Create two instances of the Point class with the coordinates (0, 3) and (4, 0) and calculate the distance of these points (use the calc_distance() method).
"""

import math

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"        

    def reset(self):
        self.x = 0
        self.y = 0

    def calc_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

point1 = Point(0, 3)
point2 = Point(4, 0)

print(point1.calc_distance(point2))
