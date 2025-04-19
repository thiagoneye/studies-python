"""
Implement a class named Pet that has two protected instance attributes: name and age, respectively.

Then, using the @property decorator, create properties: name and age, respectively
(properties to read and modify, without validation).

Create an instance of the Pet class with the name pet and attributes:
- name = 'Max'
- age = 5

Print the __dict__ attribute of the pet instance to the console.

Then modify the attributes using the dot notation:
- name to the value 'Tom'
- age to the value 8

Again, print the __dict__ attribute of the pet instance to the console again.
"""

class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

pet = Pet("Max", 5)
print(pet.__dict__)

pet.name = "Tom"
pet.age = 8
print(pet.__dict__)
