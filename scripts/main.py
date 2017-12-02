import itemLookup
import itemSearch
import goldscraper
import sys

def usage():
    print ("usage: <discount> <pages> <output filename> [category]")
    sys.exit(1

def check_discount(asin):
    titlePriceURLList = itemLookup(asin)
    camelPrice = camelCamelCamelScraper(asin)
    if (titlePriceURLList[0] / camelPrice * 100) >= sys.argv[0]:
        outFile.write("Name: " + titlePriceURLList[0] + " Amazon price: " + titlePriceURLList[1] + " Camel price " + camelPrice + " discount: " + "URL: " + titlePriceURLList[2])

def main():
    outFile = open(sys.argv[-2])
    if len(sys.argv) == 3:
        asinList = goldscraper.scrape_goldbox(sys.argv[2])
        for asin in asinList:
            check_discount(asin)
    elif len(sys.argv) == 4:
        asinResults = itemSearch.item_search(sys.argv[4], sys.argv[1])
        for item in asinResults:
            check_discount(asin)
    else:
        usage()

    outFile.close()

if __name__ == '__main__':
    main()
