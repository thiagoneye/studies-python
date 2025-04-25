"""
The following Doc class is implemented for storing text documents.

Implement the __iadd__() special method to perform extended assignments.

Concatenate two instances with the string ' & '.

Example:

    [IN]: doc1 = Doc('Finance')
    [IN]: doc2 = Doc('Accounting')
    [IN]: doc1 += doc2
    [IN]: print(doc1)

    [OUT]: Finance & Accounting

Then create two instances of the Doc class for the following documents:
- 'sport'
- 'activity'

and assign according to the variables:
- doc1
- doc2

Perform extended assignment doc1 + = doc2.

Print doc1 instance to the console.
"""

class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'
    
    def __iadd__(self, other):
        self.string += " & " + other.string
        return self

doc1 = Doc('sport')
doc2 = Doc('activity')
doc1 += doc2

print(doc1)
