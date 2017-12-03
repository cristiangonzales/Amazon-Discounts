import os
import sys; sys.path.append(
    os.path.join(os.path.dirname(__file__), "../asin/")
)



import itemLookup
import itemSearch
import goldscraper

def usage():
    print("usage: <discount> <output filename> <category | number of pages>")
    sys.exit(1)

def check_discount(discount, averagePrice, price):
    return (float(price) / float(averagePrice) * 100) >= float(discount)

def is_float(thing):
    try:
        float(thing)
        return True
    except:
        return False

def main():
    print len(sys.argv)
    assert(len(sys.argv) == 4)
    discount = sys.argv[1]
    outFile = open(sys.argv[2], 'w')
    if isinstance(sys.argv[-1],int):
        asinList = goldscraper.scrape_goldbox(sys.argv[-1]) 
    else:
        asinList = itemSearch.item_search(sys.argv[-1], discount)
    for asin in asinList:
        print 'asin is '
        print asin
        titlePriceURLList = itemLookup.item_lookup(str(asin))
        print 'discount is ' + discount + ' avg price is 1 price is ' + titlePriceURLList[1]
        if is_float(titlePriceURLList[1]) == False:
            print 'continue'
            continue
        if check_discount(discount,1,titlePriceURLList[1]):
            outFile.write("Name: " + titlePriceURLList[0] + 
                " Amazon price: " + titlePriceURLList[1] + 
                " Camel price " + '1' + " discount: " + "URL: "
                + titlePriceURLList[2] + "\n")
    outFile.close()


if __name__ == '__main__':
    main()
