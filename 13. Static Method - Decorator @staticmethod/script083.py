"""
Define a Container class that has a static method (use the staticmethod class - do it in the standard way)
named get_current_time() returning the current time in the format '%H:%M:%S', e.g. '09:45:10'.

Tip: Use the built-in time module.
"""

import time

class Container:
    def __init__(self):
        pass

    def get_current_time():
        return time.strftime("%H:%M:%S", time.localtime())

    get_current_time = staticmethod(get_current_time)

print(Container.get_current_time())
