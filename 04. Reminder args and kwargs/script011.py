"""
Implement a function called display_info() which prints the name of the company
(as shown below) and if the user also passes an argument named price, it prints
the price (as shown below).
"""

def display_info(company, **kwargs):
    print(f"Company name: {company}")
    if "price" in kwargs:
        print(f"Price: $ {kwargs['price']}")

display_info(company='CD Projekt', price=100)
