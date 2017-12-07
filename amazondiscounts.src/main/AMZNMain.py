"""
    Amazon Discount Finder. All rights reserved.
    Author: Khai Hua
    Author: Nick Leeds
"""

import logging

from amazon.api import AmazonAPI
from amazon.api import AmazonException

import os
import sys
sys.path.append(
    os.path.join(os.path.dirname(__file__), "../camelcamelcamel/")
)

import gevent.monkey
gevent.monkey.patch_thread()

from AMZNGoldboxFind import AMZNGoldboxFind
from AMZNCamelScraper import AMZNCamelScraper

"""
    This is the root class.
"""


class AMZNMain:
    # Login information and opening statements
    def __init__(self):
        # Welcome the user
        print("\n**************************************************************\n"
              + "Welcome to the Amazon-Discounts Command Line Interface (v1.0)!\n"
              + "Below are prompted instructions for your login information.\n"
              + "For the case that you might have made a mistake, please press\n"
              + "CTRL+C to start over. If anything breaks, please send a request\n"
              + "to: https://github.com/cristiangonzales/Amazon-Discounts/issues.\n"
              + "Thank you!\n"
              + "**************************************************************\n")

        # Prompt for information to log into the account
        key = input("Please enter your AWS key here: ")
        secret_key = input("Please enter your AWS secret key here: ")
        asso_tag = input("Please enter your AWS associate tag here: ")
        region = input("Please enter your region here (i.e. US, FR, CN, UK," +
                       "IN, CA, DE, JP, IT): ")
        self.amazon = AmazonAPI(
            aws_key=str(key),
            aws_secret=str(secret_key),
            aws_associate_tag=str(asso_tag),
            region=str(region).upper()
        )
        # Initialize our cart to be pointing at nothing, at first
        self.cart = None

        # Ask for the discount rate, the output file, and the option
        discount = int(input("\nPlease enter the discount you would like to query for\n"
                             + "(enter a whole number 1-99): "))
        # Check to see if it is actually an integer between 0-99
        if (not isinstance(discount, int)) or discount < 1 or discount > 99:
            raise Exception("Sorry, you did not enter a number between 1 and 99!")

        # Prompt the user for an output text file to write to
        outputFile = open("../../amazon-discounts.log", 'w')
        errorLog = open("../../failed-proxies.log", 'w')
        # Optional argument as determined by the user
        optionArg = input("Please enter a type of item you wish to search for!\n"
                          + "If you do not have a particular type of item,\n"
                          + "then enter a number so that we can search Goldbox\n"
                          + "for you and look for discounts there. Also, if you\n"
                          + "wish to search for a single item, you may enter the\n"
                          + "keywords 'item lookup': ")

        # For this option argument, if it is not a keyword, then scrape Amazon's Goldbox page,
        # and if not, then search for that item through the API. Though, if a user inputs "item
        # lookup", then simply make a single list with that ASIN number appended.
        if optionArg.isdigit():
            asinList = AMZNGoldboxFind().scrape_goldbox(int(optionArg))
        elif optionArg.replace(" ", "").upper() == "ITEMLOOKUP":
            singleItem = str(input("\nPlease enter in the ASIN number of the item you\n"
                                   + "wish to look for here: "))
            asinList = []
            asinList.append(singleItem)
        else:
            asinList = self.item_search(optionArg, discount)

        # Cart count used in the final conditional. We will do a comparison. If the counter is 0, then we will
        # use the cart_create method to create the cart, and if not, then we will use the cart_add method
        # to add to the existing cart.
        cartCount = 0
        # Iterate through the entire ASIN list to do the appropriate comparisons to see if that ASIN meets our
        # discount, and then we will write to the file
        for asin in asinList:
            # Here, we do an item lookup and get the title, current price, and offer url for this ASIN
            # In the case that the item is too low, then it will simply continue onto the next iteration
            # of the loop.
            try:
                titlePriceURLList = self.item_lookup(str(asin))
            except:
                continue
            title = titlePriceURLList[0]
            currentPrice = titlePriceURLList[1]
            offerUrl = titlePriceURLList[2]
            # Interfacing with the CamelCamelCamel scraper, passing in the ASIN number and attempting to
            # get the average, lowest, and highest price for that ASIN number. Should it be the case that
            # the average price is none, then we will check for it and see if it is accordingly.
            camelPriceHistory = AMZNCamelScraper().AccessASIN(asin)
            averagePrice = camelPriceHistory.get_average_price()
            lowestPrice = camelPriceHistory.get_lowest_price()
            highestPrice = camelPriceHistory.get_highest_price()
            # Conditional here to see if the average price is NoneType. If it is, it did not connect so we
            # should move onto the next ASIN (continue to the next iteration)
            if averagePrice is None:
                errorLog.write("Proxy tunneling failed at " + str(camelPriceHistory.get_proxy()))
                continue
            # Now, we check the discount, sending the average price, the current price, and the user's discount
            if self.check_discount(discount, averagePrice, currentPrice):
                percentageOff = self.calculate_percentage_off(averagePrice, currentPrice)
                outputFile.write("Title: " + title +
                                 "\nAmazon price: " + str(currentPrice) +
                                 "\nCamelCamelCamel average price: " + str(averagePrice) +
                                 "\nCamelCamelCamel highest price: " + str(highestPrice) +
                                 "\nCamelCamelCamel lowest price: " + str(lowestPrice) +
                                 "\nPercentage off from average: " + str(percentageOff) +
                                 "\nURL: " + offerUrl + "\n\n")
                # Logic to add this item to our cart (if it is our first time adding to the cart, then create
                # the cart item, and if it isn't the first time, then we simply add to the existiing cart
                if cartCount == 0:
                    self.cart_create(str(asin))
                    cartCount = cartCount + 1
                else:
                    self.cart_add(str(asin))
        # Write the purchase URL to the logging file
        if cartCount != 0:
            outputFile.write("Click here to add all items to your cart: " + str(self.cart.purchase_url))
        else:
            outputFile.write("Sorry, we did not find any items to add to your cart!")
        # Once we are done, close the output file and error log, and say goodbye.
        errorLog.close()
        outputFile.close()
        print("\nThank you for using the Amazon-Discounts CLI! Exiting now...\n")

    """
        Item search in the case that the user requests a query.
        :param keywords: The keyword that the user requests in the case that they want to query Amazon, as a string.
        :param pctoff: The percent off that the user requests, as an integer.
        :return: A list of ASIN values, as strings
    """

    def item_search(self, keywords, pctoff):
        try:
            result = self.amazon.search(
                SearchIndex='All', Keywords=keywords, MinPercentageOff=pctoff)
            asinList = []
            for i, product in enumerate(result):
                asinList.append(product.asin)
                # logging.debug(product.asin)
            return asinList
        except Exception as e:
            raise AmazonException(str(e))

    """
        Item lookup for the specified ASIN number.
        :param ASIN: The ASIN number, as a string.
        :return amznList [title, price, URL] as an array. Title is a string, price as a float, and URL as a string
    """

    def item_lookup(self, ASIN):
        try:
            # Initialize the Amazon list
            amznList = []
            # Lookup the result based on ASIN
            result = self.amazon.lookup(ItemId=ASIN)
            # Append the appropriate values
            amznList.append(result.title)
            # logging.debug(result.title)
            amznList.append(
                float(result.formatted_price.replace('$', ''))
            )
            # logging.debug(result.formatted_price.replace('$', ''))
            amznList.append(result.offer_url)
            # logging.debug(result.offer_url)
            # Return the list to the caller
            return amznList
        except Exception as e:
            raise AmazonException(str(e))

    """
        Check to see if this is a discount, as wanted by the user.
        :return bool (dependent on if this is a discount that we want or not).
    """

    def check_discount(self, discount, averagePrice, price):
        return (100 - (float(price) / float(averagePrice) * 100)) >= float(discount)

    """
        calculate the percentage off the current Amazon price is from the average price.
        :return int
    """

    def calculate_percentage_off(self, averagePrice, price):
        return int(100 - (float(price) / float(averagePrice) * 100))

    """
        Once we do all the appropriate comparisons, we will create the cart and
         add this item to the user's cart (this method is only used on the first ASIN).
        :param ASIN: The ASIN number of the discounted item
        :return void
    """

    def cart_create(self, ASIN):
        try:
            product = self.amazon.lookup(ItemId=ASIN)
            item = {'offer_id': product.offer_id, 'quantity': 1}
            self.cart = self.amazon.cart_create(item)
        except Exception as e:
            raise AmazonException(str(e))

    """
        This method is instantiated if we have already created the cart, and we wish to add to it.
        :param ASIN: The ASIN number of the discounted item
        :return void
    """

    def cart_add(self, ASIN):
        try:
            product = self.amazon.lookup(ItemId=ASIN)
            item = {'offer_id': product.offer_id, 'quantity': 1}
            self.amazon.cart_add(item, self.cart.cart_id, self.cart.hmac)
        except Exception as e:
            raise AmazonException(str(e))


if __name__ == "__main__":

    # Setting root logging level to DEBUG
    # logging.getLogger().setLevel(logging.DEBUG)

    # Multiple except blocks to see if the user does a keyboard interrupt, or if something breaks in the code.
    try:
        AMZNMain()
    except KeyboardInterrupt:
        print("\nExiting the CLI now...\n")
        sys.exit(1)
    except Exception as e:
        logging.error(str(e) +
                      "\nOops, sorry! Something seems to be broken." +
                      "\nPlease submit a fix request here: " +
                      "\nhttps://github.com/cristiangonzales/Amazon-Discounts/issues")
        sys.exit(1)
