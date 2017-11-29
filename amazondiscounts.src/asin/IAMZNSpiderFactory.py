"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

from interface import Interface

"""
    This is the ASIN client that employs the use of scraping spiders and webdrivers in order to display information
    and interface with the Amazon API. The logic behind implementing Selenium is to have a more robust way of
    the URL after all the appropriate filters are selected.
"""
class IAMZNSpiderFactory(Interface):

    def __init__(self):
        pass

    """
        Module that 
        :param ASIN: The ASIN number for the client to give.
        :return: An object with all the information that the client needs (specifications can be viewed in its respective
                object file).
    """
    def AccessASIN(self, ASIN):
        pass