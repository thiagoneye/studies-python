"""
The Book class is given.

Implement the __str__() method to display an informal representation of a Book instance (see below).

Example:

    [IN]: book1 = Book('Inferno', 'Dan Brown')
    [IN]: print(book1)

    [OUT]: Book ID: 214522 | Title: Inferno | Author: Dan Brown

Then create an instance named book with arguments:
- title='The Lord of the Rings'
- author='J.R.R. Tolkien'

In response, print the instance to the console.
"""

import uuid

class Book:
    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"        

    def __str__(self):
        return f"Book ID: {self.book_id} | Title: {self.title} | Author: {self.author}" 

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

book = Book("The Lord of the Rings", "J.R.R. Tolkien")
print(book)
