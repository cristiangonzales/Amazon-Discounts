"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

import logging

import sys; sys.path.append('../../../asin/')

from scrapy import Spider
from scrapy import Request
from scrapy.selector import HtmlXPathSelector

from bs4 import BeautifulSoup

"""
    This is our spider that will receive a single url to an item and scrape the prices from that website.
    Note that in settings.py (under /camelcrawler/camelcrawler/spiders), scrapy random proxy middleware has been
    enabled, as well as Autothrottling (see https://doc.scrapy.org/en/latest/topics/autothrottle.html)
"""
class AMZNCamelCrawler(Spider):

    # Identifies the spider
    name = 'AMZNCamelCrawler'

    def __init__(self, *args, **kwargs):
        super(AMZNCamelCrawler, self).__init__(*args, **kwargs)

    # Returns iterable of Requests to begin to crawl from
    def start_requests(self):
        # Create the Scrapy request with the url and parse as the callback method
        yield Request(url=self.url, callback=self.parse)

    """
        :param response: Response from the Scrapy request, from the website
    """
    def parse(self, response):
        try:
            # Get all the prices in the order of Current, Highest, Lowest, and Average
            prices = response.xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "yui3-u-1-2", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]'
            ).extract()
            # Should be 4
            logging.debug("prices length: " + str(len(prices)))

            # Employing proxy middleware
            hxs = HtmlXPathSelector(response)
            if not hxs.select('//*[(@id = "summary_chart")]'):
                yield Request(url=response.url, dont_filter=True)

        except Exception as e:
            logging.error(str(e) +
                          "\nOops, sorry! Something seems to be broken." +
                          "\nPlease submit a fix request here: " +
                          "\nhttps://github.com/cristiangonzales/Amazon-Discounts/issues")
            sys.exit(1)
