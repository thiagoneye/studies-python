"""
Implement the HouseProject class with class attributes respectively:
- number_of_floors = 3
- area = 100

Then, in the HouseProject class implement a function (class callable attribute)
called describe_project(), which displays basic information about the project.

In response, call describe_project() function.
"""

class HouseProject:
    number_of_floors = 3
    area = 100

    def describe_project():
        print(
            f'Floor number: {HouseProject.number_of_floors}\n'
            f'Area: {HouseProject.area}'
        )

HouseProject.describe_project()
