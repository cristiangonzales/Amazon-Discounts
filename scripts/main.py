import itemLookup
import itemSearch
import goldscraper
import sys

def usage():
    print ("usage: <discout> <time> [category]")
    sys.exit(1)

def main():

    if len(sys.argv) == 2:
        asin_list = goldscraper.scrape_goldbox(sys.argv[1], sys.argv[2])
        success_dictionary = {}
        for asin in asin_list:
            price_URL_tuple = itemLookup(asin)
        #   camel_price = camelCamelCamelScraper(price_URL_tuple[1])
        #   if (price_URL_tuple[0] / camel_price * 100) >= sys.argv[0]:
                #add to textfile/dictionary

    elif len(sys.argv) == 3:
        asin_results = itemSearch.itemSearch(sys.argv[3], sys.argv[1])
        for item in asin_results:
            print item

    else:
        usage()


if __name__ == '__main__':
    main()
