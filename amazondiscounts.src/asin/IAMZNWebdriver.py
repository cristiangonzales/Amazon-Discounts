"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

from interface import Interface

"""
    Interface file for the AMZNWebdriver.
    Selenium Webdriver used to navigate CamelCamelCamel website and return the url of the
    webpage that needs to be scraped to the spider.

    :var self.driver: The gdriver to navigate through the respective webpage (CamelCamelCamel primarily)
"""
class IAMZNWebdriver(Interface):

    # Constructor that initializes the webdriver.
    def __init__(self):
        pass

    """
        Set the ASIN Number for this object.
        :param number: The string ("number") to be determined by the caller (the ASIN Number)
        :return: void
    """
    def setASINNumber(self, number):
        pass

    """
        Get the ASIN Number (for debugging purposes)
        :return: The current ASIN number given to the webdriver by the caller.
    """
    def getASINNumber(self):
       pass

    """
        Using user's browser as webdriver
        :return: The url of the webpage to be scraped as a string
    """
    def CamelDriver(self):
        pass