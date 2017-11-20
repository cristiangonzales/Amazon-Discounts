"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

import logging

from tkinter import messagebox
from tkinter import Tk

from selenium import webdriver

from interface import implements

from IAMZNWebdriver import IAMZNWebdriver

"""
    Selenium Webdriver used to navigate CamelCamelCamel website and return the url of the
    webpage that needs to be scraped to the spider.

    :var self.driver: The gdriver to navigate through the respective webpage (CamelCamelCamel primarily)
"""
class AMZNWebdriver(implements(IAMZNWebdriver)):

    # Constructor that initializes the webdriver.
    def __init__(self):

        self.driver = None
        self.ASINNumber = None

        try:
            self.driver = webdriver.Chrome('../exec/chromedriver')
        except Exception as e:
            logging.error(e)
            # Error Box pop up
            errorbox = Tk()
            errorbox.withdraw()
            messagebox.showerror("ERROR", "Error message: " + str(e) +
                                 "\nOops, sorry! Something seems to be broken." +
                                 "\nPlease submit a fix request here: " +
                                 "\nhttps://github.com/cristiangonzales/Amazon-Discounts/issues")

    """
        Set the ASIN Number for this object.
        :param number: The string ("number") to be determined by the caller (the ASIN Number)
        :return: void
    """
    def setASINNumber(self, number):
        self.ASINNumber = number

    """
        Get the ASIN Number (for debugging purposes)
        :return: The current ASIN number given to the webdriver by the caller.
    """
    def getASINNumber(self):
        logging.debug("ASIN Number passed to this webdriver: " + str(self.ASINNumber))
        return self.ASINNumber

    """
        Using user's browser as webdriver
        :return: The url of the webpage to be scraped as a string
    """
    def CamelDriver(self):
        # If any attributes are invalid, the exception should return so that the user can be prompted with a message
        # to request an update/fix to the authors
        try:
            # Go to the website
            self.driver.get("https://camelcamelcamel.com/")
            self.driver.find_element_by_id("sq").send_keys(self.ASINNumber)
            self.driver.find_element_by_id("searchbutton").click()

            # Get the current URL for the spider to crawl
            url = self.driver.current_url

            logging.debug("URL of this page: " + url)

            # Close the driver
            self.driver.close()
            self.driver.quit()

            return url

        except Exception as e:
            logging.error(e)
            # Error Box pop up
            errorbox = Tk()
            errorbox.withdraw()
            messagebox.showerror("ERROR", "Error message: " + str(e) +
                                 "\nOops, sorry! Something seems to be broken." +
                                 "\nPlease submit a fix request here: " +
                                 "\nhttps://github.com/cristiangonzales/Amazon-Discounts/issues")
