import os
import sys; sys.path.append(
    os.path.join(os.path.dirname(__file__), "../asin/")
)

#from AMZNCamelScraper import AMZNCamelScraper


import itemLookup
import itemSearch
import goldscraper

def usage():
    print "usage: <discount> <output filename> <category | number of pages>"
    sys.exit(1)

def check_discount(discount, averagePrice, price):
    return (float(price) / float(averagePrice) * 100) >= float(discount)

def is_float(thing):
    try:
        float(thing)
        return True
    except ValueError:
        raise ValueError("Invalid number!")

def main():
    assert(len(sys.argv) == 4)
    discount = sys.argv[1]
    outFile = open(sys.argv[2], 'w')
    # camelObj = AMZNCamelScraper()
    if isinstance(sys.argv[-1],int):
        asinList = goldscraper.scrape_goldbox(sys.argv[-1]) 
    else:
        asinList = itemSearch.item_search(sys.argv[-1], discount)
    for asin in asinList:
        titlePriceURLList = itemLookup.item_lookup(str(asin))
        #camelPriceHistory = camelObj.AccessASIN(asin)
        #averagePrice = camelPriceHistory.get_average_price()
        print 'discount is ' + discount + ' avg price is 1 price is ' + titlePriceURLList[1]
        if is_float(titlePriceURLList[1]) == False:
            print 'continue'
            continue
        if check_discount(discount,1,titlePriceURLList[1]):
            outFile.write("Name: " + titlePriceURLList[0] + 
                " Amazon price: " + titlePriceURLList[1] + 
                " Camel price " + '1' + " discount: " + "URL: "          
                # " Camel price " + averagePrice + " discount: " + "URL: "
                + titlePriceURLList[2] + "\n")
    outFile.close()


if __name__ == '__main__':
    main()
