"""
Implement a class named TechStack that has one protected instance attribute named tech_names.

Then, using the @property decorator, create a property named tech_names (read, modify, and
delete property, without validation).

Create an instance of the class named tech_stack and the tech_names attribute value:
- 'python,java,sql'

Print the content of the tech_names attribute.

Then, modify this attribute to value:
- 'python,sql'

Also print the contents of the tech_names attribute to the console.

Remove the tech_names attribute of the tech_stack instance.

Print the contents of the __dict__ attribute of the tech_stack instance to the console.
"""

class TechStack:
    def __init__(self, tech_names):
        self._tech_names = tech_names
    
    @property
    def tech_names(self):
        return self._tech_names
    
    @tech_names.setter
    def tech_names(self, tech_names):
        self._tech_names = tech_names
    
    @tech_names.deleter
    def tech_names(self):
        del self._tech_names

tech_stack = TechStack("python,java,sql")
print(tech_stack.tech_names)

tech_stack.tech_names = "python,sql"
print(tech_stack.tech_names)

del tech_stack.tech_names
print(tech_stack.__dict__)
