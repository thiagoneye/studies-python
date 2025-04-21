"""
The Person class is implemented.

Add a special method __str__() to return an informal representation of an instance of the Person class.

Example:

    [IN]: person = Person('Mike', 'Smith')
    [IN]: print(person)

    [OUT]: First name: Mike
    [OUT]: Last name: Smith

Then create an instance named person with the following values:
- fname = 'John'
- lname = 'Doe'

In response, print the person instance to the console.
"""

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
 
    def __repr__(self):
        return f"Person(fname='{self.fname}', lname='{self.lname}')"

    def __str__(self):
        return f"First name: {self.fname}\nLast name: {self.lname}"

person = Person("John", "Doe")
print(person)
