
import unittest
from unittest.mock import patch

import os
from sys import path; path.append(
    os.path.join(os.path.dirname(__file__), "../amazondiscounts.src/camelcamelcamel/")
)
from AMZNCamelScraper import AMZNCamelScraper
from AMZNPriceHistory import AMZNPriceHistory

priceHistory = AMZNPriceHistory()
priceHistory.set_ASIN('B00YD545CC')
priceHistory.set_average_price('49.00')

class TestCamelScrapper(unittest.TestCase):
    
    def test_Camel(self):
        with patch('selenium.webdriver.Chrome') as mocked_browser:
           mocked_browser.return_value.page_source = '<table class="product_pane" width="100%"> <tbody><tr><td>Current</td>\n<td>$265.00</td>\n<td>Dec 02, 2017</td></tr><tr class="highest_price"><td>Highest <sup>*</sup></td><td>$609.99</td><td>Sep 15, 2015</td></tr><tr class="lowest_price"><td>Lowest <sup>*</sup></td><td>$265.00</td><td>Dec 02, 2017</td></tr><tr><td>Average <sup>+</sup></td><td>$276.19</td>'
           priceHistoryArray = AMZNCamelScraper().AccessASIN('hodor')
           priceObj = priceHistoryArray
           self.assertEqual(priceObj.get_ASIN(), 'hodor')
           self.assertEqual(priceObj.get_current_price(), '265.00')
           self.assertEqual(priceObj.get_highest_price(), '609.99')
           self.assertEqual(priceObj.get_lowest_price(), '265.00')
    def test_NoCurrent(self):
        with patch('selenium.webdriver.Chrome') as mocked_browser:
           mocked_browser.return_value.page_source = '<table class="product_pane" width="100%"> <tbody><tr><td>Current</td>\n<td>Not in Stock</td>\n<td>Dec 02, 2017</td></tr><tr class="highest_price"><td>Highest <sup>*</sup></td><td>$609.99</td><td>Sep 15, 2015</td></tr><tr class="lowest_price"><td>Lowest <sup>*</sup></td><td>$265.00</td><td>Dec 02, 2017</td></tr><tr><td>Average <sup>+</sup></td><td>$276.19</td>'
           priceHistoryArray = AMZNCamelScraper().AccessASIN('hodor')
           priceObj = priceHistoryArray
           self.assertEqual(priceObj.get_ASIN(), 'hodor')
           self.assertEqual(priceObj.get_current_price(), 'Not in Stock')
           self.assertEqual(priceObj.get_highest_price(), '609.99')
           self.assertEqual(priceObj.get_lowest_price(), '265.00')
           
from sys import path; path.append(
    os.path.join(os.path.dirname(__file__), "../amazondiscounts.src/main/")
)
from AMZNMain import AMZNMain

import sys

sys.stdin = open('input.txt','r')


class TestAPI(unittest.TestCase):
    def test_main(self):
        with patch('amazon.api.AmazonAPI.lookup') as mocked_lookup:
            mocked_lookup.return_value = type('obj', (object,), {'title': 'hodor', 'formatted_price': '$100.00', 'offer_url': 'hodor'})    
            with patch('AMZNCamelScraper.AMZNCamelScraper.AccessASIN') as mocked_camel:
                mocked_camel.return_value = priceHistory
                with patch('selenium.webdriver.Chrome') as mocked_browser:
                    mocked_browser.return_value.page_source = u"/dp/B00YD545CC"
                    mocked_browser.return_value.find_elements_by_partial_link_text = type('obj', (object,), {'click(self)' : True})
                    mocked_browser.return_value.execute_script = True
                    AMZNMain()                
        
        
    #def test_search(self):
    
    
    
if __name__ == "__main__":
    unittest.main()