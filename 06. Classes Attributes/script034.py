"""
A class named OnlineShop was defined with the class attributes set accordingly:
- sector to the value 'electronics'
- sector_code to the value 'ELE'
- is_public_company to the value False

Implement a function (class callable attribute) named get_sector() that returns
the value of the sector attribute of OnlineShop class. You only need to implement this function.
"""

class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False

    def get_sector():
        return OnlineShop.sector
