"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

from interface import Interface

"""
    PriceHistory class that will serve as an object to contain all the data for a given ASIN
"""
class IAMZNPriceHistory(Interface):

    def __init__(self):
        pass

    """
        Set the ASIN value for this object instance
        :param ASIN, as a string
    """
    def set_ASIN(self, ASIN):
        pass

    """
        Get the ASIN value for this object, as a string
        :return ASIN, as a string
    """
    def get_ASIN(self):
        pass

    """
        Set the current price from scraped data from our spider.
        :return None
    """
    def set_current_price(self, price):
        pass

    """
        Get the current price from scraped data from our spider.
        :return: price (or "Out of stock"), as a string
    """
    def get_current_price(self):
        pass

    """
        Set the highest price from scraped data from our spider.
        :return None
    """
    def set_highest_price(self, price):
        pass

    """
        Get the highest price from scraped data from our spider.
        :return: price, as a string
    """
    def get_highest_price(self):
        pass

    """
        Set the lowest price from scraped data from our spider.
        :return: None
    """
    def set_lowest_price(self, price):
        pass

    """
        Get the lowest price from scraped data from our spider.
        :return: price, as a string
    """
    def get_lowest_price(self):
        pass

    """
        Get the average price from scraped data from our spider.
        :return: None
    """
    def set_average_price(self,price):
        pass

    """
        Get the average price from scraped data from our spider.
        :return: price, as a string
    """
    def get_average_price(self):
        pass