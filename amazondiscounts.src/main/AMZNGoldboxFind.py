"""
    Amazon Discount Finder. All rights reserved.
    Author: Caleb Farrand
"""
import logging

import re
import time
import random

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

"""
    Iterate through Amazon's Goldbox page using a Chrome webdriver. Note here that we . Instantiates the unicode_to_ascii
    method to turn a list of ASIN numbers into ASCII values.
"""
class AMZNGoldboxFind:

    def __init__(self):
        # Initialize the options for our Chrome Driver
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")

        # Initalize our webdriver
        self.browser = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=options.to_capabilities()
        )

    def tryNextPage(self, xPixels):
        xPixelTotal = xPixels
        i = 0
        while i < 50:
            try:
                next_button = self.browser.find_elements_by_partial_link_text('Next')[0]
                self.browser.execute_script("window.scrollTo(0," + str(xPixelTotal) + ")")
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
                pass
            # Click for the next page
            numPixelScroll = 300
            success = self.tryNextPage(numPixelScroll)
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
        newArray = []
        for i in range(len(listOfStr)):
            newArray.append(str(listOfStr[i]))
            # logging.debug("ASIN number: " + str(newArray[i]))
        return newArray
