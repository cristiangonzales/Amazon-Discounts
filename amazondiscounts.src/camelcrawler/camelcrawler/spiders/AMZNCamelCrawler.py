"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

import logging
import scrapy
from bs4 import BeautifulSoup
from tkinter import messagebox, Tk

import threading
# To prevent any errors, quick fix to patch the thread
import gevent.monkey; gevent.monkey.patch_thread()

import sys
sys.path.append('../../../asin/AMZNWebdriver')

from AMZNWebdriver import AMZNWebdriver

import logging

class AMZNCamelCrawler(scrapy.Spider):

    # Identifies the spider
    name = 'AMZNCamelCrawler'

    # Returns iterable of Requests to begin to crawl from
    def start_requests(self):
        logging.debug("Value of ASIN number: " + str(self.ASIN))
        # Create an instance of a CamelCamelCamel web driver
        driver = AMZNWebdriver()
        driver.setASINNumber(self.ASIN)
        camelURL = driver.CamelDriver()

        urls = [
            camelURL
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # TODO: Web scraping logic
        pass
