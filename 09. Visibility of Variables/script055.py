"""
An implementation of the Laptop class is given. 
mplement a method called display_protected_attrs() in the Laptop class that displays the names of the protected attribute of the instance.
Then create an instance with the given arguments:

- 'Acer'
- 'Predator'
- 'AC-100'
- 5490
- 0.2

and assign it to the variable laptop.
In response, call display_protected_attrs() on the laptop instance.
"""

class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin
    
    def display_private_attrs(self):
        for attr in self.__dict__:
            if attr.startswith("_") and not attr.startswith(f"_{self.__class__.__name__}"):
                print(attr)

laptop = Laptop("Acer", "Predator", "AC-100", 5490, 0.2)
laptop.display_private_attrs()
