"""
Implement a class called Laptop that sets the following instance attributes when creating an instance:

- brand
- model
- price

When creating an instance, add validation for the price attribute. The value of the price attribute must be an int or float type greater than zero.
If it is not, raise the TypeError with the following message:

'The price attribute must be a positive int or float.'

Then create an instance called laptop with the given attributes:

- brand = 'Acer'
- model = 'Predator'
- price = 5490

In response, print the value of the __dict__ attribute of the laptop instance.
"""

class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model

        if isinstance(price, (int, float)) and price > 0:
            self.price = price
        else:
            raise TypeError("The price attribute must be a positive int or float.")

laptop = Laptop("Acer", "Predator", 5490)
print(laptop.__dict__)
