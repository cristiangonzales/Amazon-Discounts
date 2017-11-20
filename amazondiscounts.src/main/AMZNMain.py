"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

import logging

import threading

from tkinter import messagebox
from tkinter import Tk

import sys
sys.path.append("../asin/")
from AMZNAccessClient import AMZNAccessClient

"""
    This is the root class that implements all interfaces.
"""
class AMZNMain:
    def __init__(self):
        # Example of client call (for an iPhone)
        # TODO: Add Amazon API end here
        AMZNAccessClient().AccessASIN("B00YD545CC")

if __name__ == "__main__":
    # Setting root logging level to DEBUG
    logging.getLogger().setLevel(logging.DEBUG)
    try:
        mainThread = threading.Thread(target=AMZNMain)
        mainThread.start()
    except Exception as e:
        logging.error(e)
        # Error Box pop up
        errorbox = Tk()
        errorbox.withdraw()
        messagebox.showerror("ERROR", "Error message: " + str(e) +
                             "\nOops, sorry! Something seems to be broken." +
                             "\nPlease submit a fix request here: " +
                             "\nhttps://github.com/cristiangonzales/Amazon-Discounts/issues")