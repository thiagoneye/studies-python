"""
Implement a class called Laptop that sets the following instance attributes when creating an instance:

- brand as a bare instance attribute
- model as a protected attribute
- price as a private attribute

Then create an instance named laptop with the following arguments:

- 'Acer'
- 'Predator'
- 5490

In response, print the value of the __dict__ attribute of the laptop instance.
"""

class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self._price = price

laptop = Laptop("Acer", "Predator", 5490)
print(laptop.__dict__)
