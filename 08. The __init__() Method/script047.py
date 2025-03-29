"""
Implement a class called Bucket that takes any number of named arguments (keyword arguments - use **kwargs) when creating an instance.
The name of the argument is the name of the instance attribute, and the value for the argument is the value for the instance attribute.

Example:

[IN]: bucket = Bucket(apple=3.5)
[IN]: print(bucket.__dict__)
[OUT]: {'apple': 3.5}

Then create instance named bucket by adding the following attributes with their values:

- apple = 3.5
- milk = 2.5
- juice = 4.9
- water = 2.5

In response, print the value of __dict__ attribute for the bucket instance.
"""

class Bucket:

    def __init__(self, **keyargs):
        for key, value in keyargs.items():
            setattr(self, key, value)

bucket = Bucket(apple=3.5, milk=2.5, juice=4.9, water=2.5)
print(bucket.__dict__)
