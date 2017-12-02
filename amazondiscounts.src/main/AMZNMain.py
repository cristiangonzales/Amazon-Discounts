"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

import logging

import threading
import gevent.monkey; gevent.monkey.patch_thread()

import os
from sys import path; path.append(
    os.path.join(os.path.dirname(__file__), "../asin/")
)

from AMZNCamelScraper import AMZNCamelScraper

"""
    This is the root class.
"""
class AMZNMain:
    def __init__(self):
        # TODO: Add Amazon API end here
        # Example of client call (for numerous items)
        AMZNCamelScraper().AccessASIN(["B00YD545CC", "B0009VELG4", "B06XHTKFH3", "B01LWWY3E2"])

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