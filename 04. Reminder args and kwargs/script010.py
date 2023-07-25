"""
Implement a function called stick() that takes any number of bare arguments and
return an object of type str being a concatenation of all arguments of type str
passed to the function with the '#' sign (see below).
"""

def stick(*args):
    values = [value for value in args if isinstance(value, str)]
    return "#".join(values)

print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))
