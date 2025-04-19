"""
Define a Container class that has a static method (use the @staticmethod decorator) named get_current_time()
returning the current time in the format '%H:%M:%S', e.g. '09:45:10'.
"""

import time

class Container:
    def __init__(self):
        pass

    @staticmethod
    def get_current_time():
        return time.strftime("%H:%M:%S", time.localtime())
