import amazonproduct
from amazonproduct import API
import lxml
config = {
    'access_key': 'AKIAIKLBJZJSC65EHZAA',
    'secret_key': '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',
    'associate_tag': 'kdhua-20',
    'locale': 'us'
}
def itemLookup(asin):
  api = amazonproduct.API(cfg=config)
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
