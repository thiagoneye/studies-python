"""
A global variable counter is given with an incorrectly implemented update_counter() function.
Correct the implementation of the update_counter() function so that you can modify the
counter variable from this function. Then call the update_counter() function.
"""

counter = 1

def update_counter():
    global counter
    counter += 1

update_counter()
print(counter)
