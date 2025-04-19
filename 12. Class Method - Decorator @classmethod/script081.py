"""
Implement a class named Person which has a class attribute named instances as an empty list.
Then, each time you create an instance of the Person class, add it to the Person.instances list (use the __init __() method for this).

Also implement a class method called count_instances() that returns the number of Person objects created (the number of items in the Person.instances list).

Create three instances of the Person class.
Then call the count_instances() class method and print result to the console.
"""

class Person:

    instances = []

    def __init__(self):
        Person.instances.append(self)
    
    @classmethod
    def count_instances(cls):
        return len(cls.instances)
    
p1 = Person()
p2 = Person()
p3 = Person()

print(Person.count_instances())
