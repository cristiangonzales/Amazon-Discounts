import amazonproduct
from amazonproduct import API
import lxml
}

def itemLookup(asin):
  api = amazonproduct.API(cfg=~/.credential)
  result = api.item_lookup(asin, ResponseGroup= 'Large')

  for item in result.Items.Item:
    print (item.ItemAttributes.Title)
    print (item.OfferSummary.LowestNewPrice.FormattedPrice)
    print (item.DetailPageURL)
    return (item.ASIN)

  
def main():
  itemLookup('B00V2L5JRA')

if __name__ == '__main__':
  main()
