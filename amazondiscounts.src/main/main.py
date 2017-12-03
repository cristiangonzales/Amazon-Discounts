import os
import sys; sys.path.append(
    os.path.join(os.path.dirname(__file__), "../asin/")
)

from AMZNCamelScraper import AMZNCamelScraper

import itemLookup
import itemSearch
import goldscraper

def usage():
    print "usage: <discount> <output filename> <category | number of pages>"
    sys.exit(1)

def check_discount(discount, averagePrice, price):
    return (price / averagePrice * 100) >= discount

def main():
    try: 
        assert(len(sys.argv) == 4)
        discount = sys.argv[1]
        outFile = open(sys.argv[2])
        camelObj = AMZNCamelScraper()
        if isinstance(sys.argv[-1],int):
            asinList = goldscraper.scrape_goldbox(sys.argv[-1]) 
        else:
            asinList = itemSearch.item_search(sys.argv[-1], discount)
        for asin in asinList:
            titlePriceURLList = itemLookup.item_lookup(asin)
            camelPriceHistory = camelObj.AccessASIN(asin)
            averagePrice = camelPriceHistory.get_average_price()
            if check_discount(discount,averagePrice,titlePriceURLList[1]):
                outFile.write("Name: " + titlePriceURLList[0] + 
                    " Amazon price: " + titlePriceURLList[1] + 
                    " Camel price " + averagePrice + " discount: " + "URL: "
                    + titlePriceURLList[2])
        outFile.close()
    except:
        usage()

if __name__ == '__main__':
    main()
