"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

import logging

import sys
sys.path.append('../camelcrawler/camelcrawler')
sys.path.append('../camelcrawler/camelcrawler/spiders')

from interface import implements

from tkinter import messagebox
from tkinter import Tk

from IAMZNAccessClient import IAMZNAccessClient
from AMZNCamelCrawler import AMZNCamelCrawler
from scrapy.crawler import CrawlerProcess

"""
    This is the class that employs the use of scraping spiders and webdrivers in order to obtain information to be
    passed to the client that is using the Amazon API calls. The logic behind implementing Selenium is to have a more
    robust way of obtaining the URL after all the appropriate filters have been selected.
"""
class AMZNAccessClient(implements(IAMZNAccessClient)):

    def __init__(self):
        pass

    """
        Module that 
        :param ASIN: The ASIN number for the client to give.
        :return: An object with all the information that the client needs (specifications can be viewed in its respective
                object file).
    """
    def AccessASIN(self, ASIN):
        try:
            # Crawler process
            process = CrawlerProcess({'SPIDER_MODULES': 'spiders'})
            process.crawl(AMZNCamelCrawler, ASIN=ASIN)
            process.start()
        except Exception as e:
            logging.error(e)
            # Error Box pop up
            errorbox = Tk()
            errorbox.withdraw()
            messagebox.showerror("ERROR", "Error message: " + str(e) +
                                 "\nOops, sorry! Something seems to be broken." +
                                 "\nPlease submit a fix request here: " +
                                 "\nhttps://github.com/cristiangonzales/Amazon-Discounts/issues")