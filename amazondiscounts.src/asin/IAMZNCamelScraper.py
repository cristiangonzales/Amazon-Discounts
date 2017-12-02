"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

from interface import Interface

"""
    This is the class that employs the use of a webdriver in order to obtain information to be
    passed to the client that is using the Amazon API calls. The logic behind implementing Selenium is to outsmart
    the Distil Networks server, wait for the JavaScript to load after our first request (using a randomized wait
    time), and then create a second request to obtain the appropriate HTML source.
"""
class IAMZNCamelScraper(Interface):

    def __init__(self):
        pass

    """
        Module that is to be used to access the page source and store all the data inside a PriceHistory object,
        and an array of PriceHistory objects is to be passed back to the caller.
        :param arrayOfASIN: An array of ASIN numbers for the client to give, as strings
        :return: An object with all the information that the client needs (details can be viewed in its respective
                object file).
    """
    def AccessASIN(self, arrayOfASIN):
        pass

    """
        Module employed by AccessASIN that takes HTML source and will parse the highest, lowest, current, and average
        prices from the CamelCamelCamel site using regular expressions.
        :param html: The HTML source to be passed for a single Amazon item
        :param ASIN: The ASIN number associated with this item.
        :return AMZNPriceHistory object to the caller
    """
    def parse(self, html, ASIN):
        pass

    """
        Select a random proxy as a string to be selected for our Chrome Driver options. Proxies
        may be HTTP or HTTPS.
    """
    def select_proxy_server(self):
        pass