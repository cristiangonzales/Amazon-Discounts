"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

from interface import implements

import logging

from IAMZNPriceHistory import IAMZNPriceHistory

"""
    PriceHistory class that will serve as an object to contain all the data for a given ASIN
"""
class AMZNPriceHistory(implements(IAMZNPriceHistory)):

    def __init__(self):
        self.ASIN = None
        self.current_price = None
        self.highest_price = None
        self.lowest_price = None
        self.average_price = None

    """
        Set the ASIN value for this object instance
        :param ASIN, as a string
    """
    def set_ASIN(self, ASIN):
        self.ASIN = ASIN

    """
        Get the ASIN value for this object, as a string
        :return ASIN, as a string
    """
    def get_ASIN(self):
        logging.debug("ASIN number of this object: " + self.ASIN)
        return self.ASIN

    """
        Set the current price from scraped data from our spider.
        :return None
    """
    def set_current_price(self, price):
        self.current_price = price

    """
        Get the current price from scraped data from our spider.
        :return: price, as a string
    """
    def get_current_price(self):
        logging.debug("Current price of " + self.ASIN + ": " + self.current_price)
        return self.current_price

    """
        Set the highest price from scraped data from our spider.
        :return None
    """
    def set_highest_price(self, price):
        self.highest_price = price

    """
        Get the highest price from scraped data from our spider.
        :return: price, as a string
    """
    def get_highest_price(self):
        logging.debug("Highest price of " + self.ASIN + ": " + self.highest_price)
        return self.highest_price

    """
        Set the lowest price from scraped data from our spider.
        :return: None
    """
    def set_lowest_price(self, price):
        self.lowest_price = price

    """
        Get the lowest price from scraped data from our spider.
        :return: price, as a string
    """
    def get_lowest_price(self):
        logging.debug("Lowest price of " + self.ASIN + ": " + self.lowest_price)
        return self.lowest_price

    """
        Get the average price from scraped data from our spider.
        :return: None
    """
    def set_average_price(self, price):
        self.average_price = price

    """
        Get the average price from scraped data from our spider.
        :return: price, as a string
    """
    def get_average_price(self):
        logging.debug("Average price of " + self.ASIN + ": " + self.average_price)
        return self.average_price