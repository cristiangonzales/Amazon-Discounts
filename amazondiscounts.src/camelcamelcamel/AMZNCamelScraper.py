"""
    Amazon Discount Finder. All rights reserved.
    Author: Chris Evans
"""

import logging

import os
import sys

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import random
import time

from bs4 import BeautifulSoup
import re
from AMZNPriceHistory import AMZNPriceHistory

"""
    This is the class that employs the use of a webdriver in order to obtain information to be
    passed to the client that is using the Amazon API calls. The logic behind implementing Selenium is to outsmart
    the Distil Networks server, wait for the JavaScript to load after our first request (using a randomized wait
    time), and then create a second request to obtain the appropriate HTML source.
"""
class AMZNCamelScraper:

    def __init__(self):

        # Initialize class variable for proxy
        self.proxy = self.select_proxy_server()

        # Initialize the options for our Chrome Driver
        options = Options()
        options.add_argument('--proxy-server=' + self.proxy)
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")

        # Initalize our webdriver
        self.browser = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=options.to_capabilities()
        )

    """
        Module that is to be used to access the page source and store all the data inside a PriceHistory object,
        and a single PriceHistory object is to be passed back to the caller.
        :param ASIN: The ASIN number for the client to give.
        :return: An object with all the information that the client needs (details can be viewed in its respective
                object file).
    """
    def AccessASIN(self, ASIN):
        try:
            # First request to camelcamelcamel (expects Distil Networks pop-up, which we don't actually use)
            self.browser.get("https://camelcamelcamel.com/search?sq=" + ASIN)

            # Wait time before the second request
            waitTime = random.uniform(7, 12)
            time.sleep(waitTime)
            # Make a second request to get the source (this time successful)
            html = self.browser.page_source
            # Close and quit the browser
            self.browser.close()
            self.browser.quit()
            # Return the final PriceHistory object to the caller
            return self.parse(html, ASIN)

        except Exception as e:
            logging.error(str(e) +
                          "\nOops, sorry! Something seems to be broken." +
                          "\nPlease submit a fix request here: " +
                          "\nhttps://github.com/cristiangonzales/Amazon-Discounts/issues")
            sys.exit(1)

    """
        Module employed by AccessASIN that takes HTML source and will parse the highest, lowest, current, and average
        prices from the CamelCamelCamel site using regular expressions.
        :param html: The HTML source to be passed
        :return AMZNPriceHistory object to the caller
    """
    def parse(self, html, ASIN):
        try:
            # Declare new object instance
            obj = AMZNPriceHistory()
            # Declare the proxy value for this object
            obj.set_proxy(self.proxy)
            # Set the ASIN number for this object
            obj.set_ASIN(ASIN)
            # Create new soup instance with the source passed from the caller
            soup = BeautifulSoup(html, "html.parser")

            # Set the current price
            _soupStr = str(soup.find(class_="product_pane"))

            # Here, we do nested try-except blocks. For the case that we cannot find a dollar amount
            # for the current price, we will try to find the string "Not in stock." For any strange
            # anomaly that it is not a dollar amount or "Not in stock", we will simply pass this and
            # set leave it to NoneType, as initially defined in the PriceHistory constructor.
            try:
                # Now search for a subset, which would be the actual price value
                tempStr = re.search('<td>Current<\/td>\n<td>*.*', _soupStr).group(0)
                currentPrice = re.search('\$[0-9]*\.[0-9]{2}', tempStr).group(0)[1:]
                # logging.debug("Current price for " + ASIN + ": " + currentPrice)
                obj.set_current_price(currentPrice)
            except:
                # In the case that the item is not in stock, do a regex search for "Not in Stock".
                # For any extra anomalies, simply pass it
                try:
                    tempStr = re.search('<td>Current<\/td>\n<td>*.*', _soupStr).group(0)
                    currentPrice = re.search('Not in Stock', tempStr).group(0)
                    # logging.debug("Current price for " + ASIN + ": " + currentPrice)
                    obj.set_current_price(currentPrice)
                except Exception as e:
                    # logging.error(e)
                    pass

            # Try to find the highest price. If it does not exist for this item, we will leave it to
            # NoneType as defined in the obj's constructor
            try:
                _soupStr = str(soup.find(class_="highest_price"))
                highestPrice = re.search('\$[0-9]*\.[0-9]{2}', _soupStr).group(0)[1:]
                # logging.debug("Highest price for " + ASIN + ": " + highestPrice)
                # Store the value as a string
                obj.set_highest_price(highestPrice)
            except Exception as e:
                # logging.error(e)
                pass

            # Try to find the highest price. If it does not exist for this item, we will leave it to
            # NoneType as defined in the obj's constructor
            try:
                _soupStr = str(soup.find(class_="lowest_price"))
                lowestPrice = re.search('\$[0-9]*\.[0-9]{2}', _soupStr).group(0)[1:]
                # logging.debug("Lowest price for " + ASIN + ": " + lowestPrice)
                # Store the value as a string
                obj.set_lowest_price(lowestPrice)
            except Exception as e:
                # logging.error(e)
                pass

            # Try to find the average price. If it does not exist for this item, we will leave it to
            # NoneType as defined in the obj's constructor
            try:
                _soupStr = str(soup.find(class_="product_pane"))
                # Search for "Current" source
                tempStr = re.search('<td>Average <sup>\+<\/sup><\/td>\n*.*', _soupStr).group(0)
                # Now search for a subset, which would be the actual price value
                averagePrice = re.search('\$[0-9]*\.[0-9]{2}', tempStr).group(0)[1:]
                # logging.debug("Average price for " + ASIN + ": " + averagePrice)
                # Store the value as a string
                obj.set_average_price(averagePrice)
            except Exception as e:
                # logging.error(e)
                pass

            # Return the final object to the caller
            return obj

        except Exception as e:
            logging.error(str(e) +
                          "\nOops, sorry! Something seems to be broken." +
                          "\nPlease submit a fix request here: " +
                          "\nhttps://github.com/cristiangonzales/Amazon-Discounts/issues")
            sys.exit(1)

    """
        Select a random proxy as a string to be selected for our Chrome Driver options. Proxies
        may be HTTP or HTTPS.
        :return random proxy as a string
    """
    def select_proxy_server(self):
        # Configure the relative path so that we can open the file
        path_to_proxylist = os.path.join(os.path.dirname(__file__), '../../proxy-list.txt')
        random_proxy = random.choice(
            open(path_to_proxylist).readlines()
        )
        # logging.info("Random proxy: " + random_proxy)
        return random_proxy