"""
The people list is given.

Sort the objects in the people list ascending by age.

Then print the name and age to the console as shown below.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person('Tom', 25), Person('John', 29),
          Person('Mike', 27), Person('Alice', 19)]

people.sort(key=lambda person: person.age)

for person in people:
    print(f"{person.name} -> {person.age}")
