"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

import logging

import sys

import threading
import gevent.monkey; gevent.monkey.patch_thread()

from sys import path; path.append("../asin/")

from AMZNCamelScraper import AMZNCamelScraper

"""
    This is the root class.
"""
class AMZNMain:
    def __init__(self):
        # TODO: Add Amazon API end here
        # Example of client call (for numerous items)
        asinArr = ["B00YD545CC", "B0009VELG4", "B06XHTKFH3", "B01LWWY3E2"]
        AMZNCamelScraper().AccessASIN(asinArr)

if __name__ == "__main__":
    # Setting root logging level to DEBUG
    logging.getLogger().setLevel(logging.DEBUG)
    try:
        mainThread = threading.Thread(target=AMZNMain)
        mainThread.start()
    except Exception as e:
        logging.error(str(e) +
                      "\nOops, sorry! Something seems to be broken." +
                      "\nPlease submit a fix request here: " +
                      "\nhttps://github.com/cristiangonzales/Amazon-Discounts/issues")
        sys.exit(1)