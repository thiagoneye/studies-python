"""
A class called Laptop was implemented.
Try to create an instance named laptop with the given attribute values:

- brand = 'Acer'
- model = 'Predator'
- price = '5900'

Note that in this case the value of the price attribute is passed as a str type.
In case of error, print the error message to the console (use the try ... except ... clause).
"""

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        
        if isinstance(price, (int, float)) and price > 0:
            self.price = price
        else:
            raise TypeError('The price attribute must be a positive int or float.')

try:
    laptop = Laptop("Acer", "Predator", "5900")
except TypeError as error:
    print(error)
