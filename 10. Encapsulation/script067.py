"""
Implement a class named Pet that has one protected instance attribute name.

Then, using the @property decorator, create a property name (property to read and modify, without validation).

Create an instance of the Pet class named pet and set the name attribute to 'Max'.
Then, using dot notation, modify the value of the name attribute to 'Oscar'.

In response, print the contents of the __dict__ attribute of this instance to the console.
"""

class Pet:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

pet = Pet("Max")
pet.name = "Oscar"
print(pet.__dict__)
