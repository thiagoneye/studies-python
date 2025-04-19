"""
Using the @classmethod decorator, implement a class named Container which has a class method named show_details() displaying the following text to the console:
- 'Running from Container class.'

Try to pass the class name using the appropriate attribute of the Container class.

In response, call the show_details() class method.
"""

class Container:
    def __init__(self):
        pass

    @classmethod
    def show_details(cls):
        print(f"Running from {cls.__name__} class.")
    
Container().show_details()
