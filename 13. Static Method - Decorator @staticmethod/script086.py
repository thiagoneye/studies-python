"""
The Book class is implemented.

Add a __repr__() method to the Book class that represents an instance of this class (see below).

Then create an instance of the class named book1 passing the following arguments:
- title='Inferno'
- author='Dan Brown'

In response, print the instance book1 to the console.
"""

import uuid

class Book:
    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

book1 = Book('Inferno', 'Dan Brown')
print(book1)
