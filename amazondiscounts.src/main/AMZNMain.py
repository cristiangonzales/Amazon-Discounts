"""
Amazon Discount Finder. All rights reserved.
Author: Cristian Gonzales
"""

import logging

import sys
sys.path.append('../camelcrawler/camelcrawler')
from tkinter import messagebox, Tk
# Scrapy API
from scrapy.crawler import CrawlerProcess

"""
    This is the main method that employs the use of scraping spiders and webdrivers in order to display information
    and interface with the Amazon API. The logic behind implementing Selenium is to have a more robust way of
    the URL after all the filters are selected.
"""
def main():

    try:
        # Crawler process
        process = CrawlerProcess({'SPIDER_MODULES': 'spiders'})
        process.crawl("AMZNCamelCrawler")
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

if __name__ == "__main__":
    main()