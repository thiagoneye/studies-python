"""
The Product class is given below. Display the namespace
(value of the __dict__ attribute) of this class as shown below.
"""

import uuid

class Product:

    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return (
            f"Product(product_name='{self.product_name}', "
            f"price={self.price})"
        )

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


if __name__ == "__main__":
    for name in Product.__dict__:
        print(name)
