"""
Two empty classes are defined:
- Model
- View

Using the built-in function issubclass() check if the classes Model and View are
derived classes (subclasses) of the built-in object class.
"""

class Model:
    pass

class View:
    pass

print(issubclass(Model, object))
print(issubclass(View, object))
