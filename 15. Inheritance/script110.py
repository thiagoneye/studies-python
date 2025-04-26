"""
The following classes are implemented:
- Vehicle
- LandVehicle
- AirVehicle

Define a display_info() method in the Vehicle class to display
the class name along with the value of the category attribute.

The method is supposed to work for all classes.
"""

class Vehicle:
    def __init__(self, category=None):
        self.category = category if category else 'land vehicle'
    
    def display_info(self):
        print(f"{self.__class__.__name__} -> {self.category}")
    
class LandVehicle(Vehicle):
    pass

class AirVehicle(Vehicle):
    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'

vehicles = [Vehicle(), LandVehicle(), AirVehicle()]

for vehicle in vehicles:
    vehicle.display_info()
