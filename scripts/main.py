import itemLookup
import itemSearch
import goldscraper
import ../amazondiscounts.src/asin/AMZNCamelScraper
import sys

def usage():
    print ("usage: <discount> <output filename> <category | number of pages>")
    sys.exit(1)

def check_discount(discount, asin, camelObj, price):
    camelPriceHistory = camelObj.AccessASIN(asin)
    camelPrice = camelPriceHistory.get_average_price()
    return (price / camelPrice * 100) >= discount

def main():
    try: 
        assert(len(sys.argv) == 4)
        discount = sys.argv[1]
        outFile = open(sys.argv[2])
        camelObj = AMZNCamelScraper.AMZNCamelScraper()
        if isinstance(argv[-1],int):
            asinList = goldscraper.scrape_goldbox(sys.argv[-1])
            for asin in asinList:
                titlePriceURLList = itemLookup.item_lookup(asin)
                if check_discount(discount,asin,camelObj,titlePriceURLList[1]):
                    outFile.write("Name: " + titlePriceURLList[0] + 
                        " Amazon price: " + titlePriceURLList[1] + 
                        " Camel price " + camelPrice + " discount: " + "URL: " 
                        + titlePriceURLList[2])
        else:
            asinResults = itemSearch.item_search(sys.argv[-1], discount)
            for item in asinResults:
                titlePriceURLList = itemLookup.item_lookup(asin)
                if check_discount(discount,asin,camelObj,titlePriceURLList[1]):
                    outFile.write("Name: " + titlePriceURLList[0] + 
                        " Amazon price: " + titlePriceURLList[1] + 
                        " Camel price " + camelPrice + " discount: " + "URL: " 
                        + titlePriceURLList[2])
        outFile.close()
    except:
        print usage

if __name__ == '__main__':
    main()
