"""
Create a class named CustomDict that extends the built-in dict class.

Add a method named is_any_str_value() that returns a boolean value:
- True in case the created dictionary contains at least one value of str type
- otherwise False.
"""

class CustomDict(dict):
    def is_any_str_value(self):
        return any(isinstance(value, str) for value in self.values())

if __name__ == "__main__":
    cd = CustomDict(python="mid")
    print(cd.is_any_str_value())

    cd = CustomDict(price=119.99)
    print(cd.is_any_str_value())


