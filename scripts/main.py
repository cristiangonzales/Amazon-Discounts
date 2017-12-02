import itemLookup
import itemSearch
import goldscraper
import sys

def usage():
    print ("usage: <discout> <pages> <output filename> [category]")
    sys.exit(1

def checkDiscount(asin):
    title_price_URL_list = itemLookup(asin)
    camel_price = camelCamelCamelScraper(asin)
    if (price_URL_tuple[0] / camel_price * 100) >= sys.argv[0]:
        out_file.write("Name: " + title_price_URL_list[0] + " Amazon price: " + title_price_URL_list[1] + " Camel price " + camel_price + " discount: " + "URL: " + title_price_URL_list[2])

def main():
    out_file = open(sys.argv[-2])
    if len(sys.argv) == 3:
        asin_list = goldscraper.scrape_goldbox(sys.argv[2])
        for asin in asin_list:
            checkDiscount(asin)
    elif len(sys.argv) == 4:
        asin_results = itemSearch.itemSearch(sys.argv[4], sys.argv[1])
        for item in asin_results:
            checkDiscount(asin)
    else:
        usage()

    out_file.close()

if __name__ == '__main__':
    main()
