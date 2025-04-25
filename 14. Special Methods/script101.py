"""
The following Hashtag class is implemented for storing text documents - hashtags.

Implement the __add__() special method to add (concatenate) Hashtag instances using
a space character as shown below (take into account the appropriate number of '#'
characters at the beginning of the new object).

Example:

    [IN]: hashtag1 = Hashtag('sport')
    [IN]: hashtag2 = Hashtag('travel')
    [IN]: print(hashtag1 + hashtag2)

    [OUT]: #sport #travel

Then create three Hashtag instances for the following text documents:
- python
- developer
- oop

In response, print the result of adding these instances.
"""

class Hashtag:
    def __init__(self, string):
        self.string = '#' + string

    def __repr__(self):
        return f"Hashtag(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'
    
    def __add__(self, other):
        return Hashtag(self.string[1:] + " " + other.string)

hash1 = Hashtag('python')
hash2 = Hashtag('developer')
hash3 = Hashtag('oop')
print(hash1 + hash2 + hash3)
