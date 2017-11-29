"""
    Amazon Discount Finder. All rights reserved.
    Author: Cristian Gonzales
"""

import logging
from scrapy import Spider
from scrapy import Request
from random import random
from random import choice
from bs4 import BeautifulSoup

import sys
sys.path.append('../../../asin/AMZNWebdriver')

import logging

class AMZNCamelCrawler(Spider):

    # Identifies the spider
    name = 'AMZNCamelCrawler'

    # Initialization to
    def __init__(self, *args, **kwargs):
        super(AMZNCamelCrawler, self).__init__(*args, **kwargs)
        self.proxy_pool = ['http://110.139.118.95:8080', 'https://202.170.83.212:3128', 'http://41.0.57.69:3128',
                           'https://177.223.6.13:8080', 'https://190.13.172.170:8080', 'http://190.207.156.165:8080',
                           'http://186.92.87.226:8080', 'https://176.194.189.56:8080', 'https://62.165.42.170:8080',
                           'http://216.40.252.91:3128', 'https://118.97.20.19:8080', 'https://182.50.64.71:8080',
                           'https://91.214.84.110:3128', 'https://223.27.151.141:3128', 'https://124.124.55.197:8080',
                           'https://41.207.116.17:3128', 'https://200.8.230.80:8080', 'https://201.62.57.1:8080',
                           'https://193.193.68.2:8080', 'https://202.166.198.130:80', 'http://201.20.177.185:8080',
                           'http://91.217.67.248:80', 'https://66.171.176.58:8080', 'http://190.0.60.238:3128',
                           'https://69.73.181.24:7808', 'http://12.199.141.164:80', 'http://72.253.174.248:8080',
                           'http://37.206.58.158:8080', 'http://94.228.192.81:8080', 'https://84.22.2.65:8080',
                           'http://190.146.132.205:8080', 'https://173.213.113.111:8089', 'http://119.110.71.126:8080']

    # Returns iterable of Requests to begin to crawl from
    def start_requests(self):
        # Create the Scrapy request with the url and the parse as the callback method
        request = Request(url=self.url, callback=self.parse)
        # Initialize a new proxy
        if self.proxy_pool:
            request.meta['proxy'] = choice(self.proxy_pool)
            yield request

    """
        :param response: Response from the Scrapy request, from the website
    """
    def parse(self, response):
        pass
