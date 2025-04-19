"""
Implement a class named Rectangle which will have the following properties:
- width
- height

The width and height of the rectangle, respectively (for reading and for modification).

Also add a property named area that stores the area of the rectangle (read-only).
This property should be computed only at the first reading or after modifying any of the rectangle sides.

Skip attribute validation.

Then create an instance named rectangle with a width = 3 and a height = 4 and print the information about the rectangle instance to the console as shown below.
"""

class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._area = None

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value
    
    @property
    def area(self):
        self._area = self._width * self._height
        return self._area

rectangle = Rectangle(3, 4)
print(f"width: {rectangle.width}, height: {rectangle.height} -> area: {rectangle.area}")
