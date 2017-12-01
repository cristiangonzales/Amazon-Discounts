import amazonproduct
from amazonproduct import API
import lxml
config = {
    'access_key': 'AKIAIKLBJZJSC65EHZAA',
    'secret_key': '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',
    'associate_tag': 'kdhua-20',
    'locale': 'us'
}

# input: Asin
# output [title, price, URL]
def itemLookup(asin):
  api = amazonproduct.API(cfg=config)
  result = api.item_lookup(asin, ResponseGroup= 'Large')
  l = []
  # this for loop will only execute once.
  for item in result.Items.Item:
    l.append(item.ItemAttributes.Title)
    l.append(item.OfferSummary.LowestNewPrice.FormattedPrice)
    l.append(item.DetailPageURL)
    return l
