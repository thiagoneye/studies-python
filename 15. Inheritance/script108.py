"""
The following classes are implemented:
- Container
- PlasticContainer
- MetalContainer
- SmallPlasticContainer

Print the MRO - Method Resolution Order for SmallPlasticContainer class.

Note: The solution that the user passes is in a file named exercise.py,
while the checking code (which is invisible to the user) is executed from
a file named evaluate.py from the level where the classes are imported.
Therefore, instead of the name of the module __main__, the response will
be the name of the module in which this class is implemented, in this case
exercise.
"""

class Container:
    pass

class PlasticContainer(Container):
    pass

class MetalContainer(Container):
    pass

class SmallPlasticContainer(PlasticContainer):
    pass

print(SmallPlasticContainer.mro())
