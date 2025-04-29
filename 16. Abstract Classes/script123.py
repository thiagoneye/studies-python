"""
Create an abstract class named Figure with the abstract method named area.

Then create a Square class that inherits from the Figure class, which sets the side length of the square in the constructor.

Implement the area method that allows you to calculate the area of a square.

Then try to create an instance of the Figure class, in case of an error, print the error message to the console.
"""

from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Figure):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        self.area = self.length**2

try:
    figure = Figure()
except Exception as error:
    print(error)
