"""
    Amazon Discount Finder. All rights reserved.
    Author: Caleb Farrand
"""
import logging

import re
import time
import random

import os
from platform import system
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

from selenium import webdriver

"""
    Iterate through Amazon's Goldbox page using a Chrome webdriver. Note here that we . Instantiates the unicode_to_ascii
    method to turn a list of ASIN numbers into ASCII values.
"""
class AMZNGoldboxFind:

    def __init__(self):
        # TODO: Initialize the options for our Chrome Driver
        options = Options()
        options.add_argument('--window-size=' )

        # See the user's system information, and choose the appropriate webdriver executable, accordingly
        if system() == "Darwin":
            # Configure the path
            chrome_path = os.path.join(os.path.dirname(__file__), '../chromedriver/darwin/chromedriver')
            # Initialize our web driver
            self.browser = webdriver.Chrome(
                executable_path=chrome_path
                # chrome_options=
            )
        elif system() == "Linux":
            # Configure the path
            chrome_path = os.path.join(os.path.dirname(__file__), '../chromedriver/linux/chromedriver')
            # Initialize our web driver
            self.browser = webdriver.Chrome(
                executable_path=chrome_path
                # chrome_options=
            )
        elif system() == "Windows":
            # Configure the path
            chrome_path = os.path.join(os.path.dirname(__file__), '../chromedriver/windows/chromedriver.exe')
            # Initialize our web driver
            self.browser = webdriver.Chrome(
                executable_path=chrome_path
                # chrome_options=
            )
        else:
            raise WebDriverException(
                'Incompatible system requirements. Please see: https://github.com/cristiangonzales' +
                '/Amazon-Discounts/wiki/Installation'
            )

    def tryNextPage(self, xPixels):
        xPixelTotal = xPixels
        i = 0
        while i < 10:
            try:
                next_button = self.browser.find_elements_by_partial_link_text('Next')[0]
                self.browser.execute_script("window.scrollTo(0," + xPixelTotal + ")")
                next_button.click()
                return True
            except:
                xPixelTotal += xPixels
            i += 1
        return False


    """
        Scraping Goldbox. Instantiates the unicode_to_ascii method in order to return a list of ASIN strings
        to the caller.
        :param numOfPages: The number of pages to scrape, as defined by the caller (this is the case where
        the user does not enter a query for an amount of pages to find).
    """
    def scrape_goldbox(self, numOfPages):
        # Instantiate the web driver
        self.browser.get("https://www.amazon.com/gp/goldbox")
        asins = []
        j = 0
        # Upper bounds is the number of pages, as requested by the user
        while (j < numOfPages):
            strOfContent = self.browser.page_source
            # Attempt to find a regular expression for the ASIN number
            try:
                pattern = "/dp/[0-9|A-Z]{9,11}"
                result = re.findall(pattern, strOfContent)
                for i in range(len(result)):
                    item = result[i].replace("/dp/", "")
                    result[i] = item
                result = list(set(result))
                asins = asins + result
            except Exception as e:
                logging.error("Error: unable to connect to Goldbox for scraping. Error: " + e)
            # Click for the next page
            numPixelScroll = 300
            tryNextPage(numPixelScroll)
            # next_button = self.browser.find_elements_by_partial_link_text('Next')[0]
            # self.browser.execute_script("window.scrollTo(0,4687)")
            # next_button.click()
            j += 1
            time.sleep(random.random() * 10)
        self.browser.close()
        self.browser.quit()

        return self.unicode_to_ascii(asins)

    """
        As implied, turns a list of unicode values (the ASIN values) and turns each element into ASCII
        :listOfStr: The list of unicode values (ASIN) to be returned to the original caller of this class.
    """
    def unicode_to_ascii(self, listOfStr):
        for i in range(len(listOfStr)):
            asciiStr = listOfStr[i].encode('utf-8', errors='backslashreplace')
            listOfStr[i] = asciiStr
        return listOfStr
