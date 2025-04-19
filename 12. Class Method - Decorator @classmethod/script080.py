"""
The Container class is given.

Create an instance of this class named container and call the show_details() method from this instance.
"""

class Container:
    def __init__(self):
        pass

    @classmethod
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')

container = Container()
container.show_details()
