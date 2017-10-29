"""
Amazon Discount Finder. All rights reserved.
Author: Cristian Gonzales
"""

import scrapy


class AMZNCamelCrawler(scrapy.Spider):
    name = 'AMZNCamelCrawler'
    allowed_domains = ['https://camelcamelcamel.com/']
    start_urls = ['http://https://camelcamelcamel.com//']

    def parse(self, response):
        pass
