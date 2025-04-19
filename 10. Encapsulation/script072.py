"""
Implement a class Game that has a property named level (read and modify property, defaults to 0).

The value of the level attribute should be an integer in the range [0, 100].
Add validation at the instance creation and attribute modification stage.

If the value is not of the int type, raise a TypeError with the following message:
- 'The value of level must be of type int.'

If the value is outside the range [0, 100], set the exceeded boundary value (0 or 100 respectively).

Then create a list called games consisting of four instances of the Game class:
- games = [Game(), Game(10), Game(-10), Game(120)]

Iterate through the games list and print the value of the level attribute for each instance.
"""

class Game:
    def __init__(self, value=0):
        if not isinstance(value, int):
            raise TypeError("The value of level must be of type int.")
        elif value < 0:
            self._level = 0
        elif value > 100:
            self._level = 100
        else:
            self._level = value
    
    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        if not isinstance(value, int):
            raise TypeError("The value of level must be of type int.")
        elif value < 0:
            self._level = 0
        elif value > 100:
            self._level = 100
        else:
            self._level = value

games = [Game(), Game(10), Game(-10), Game(120)]

for game in games:
    print(game.level)
