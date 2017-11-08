import amazonproduct
from amazonproduct import API
import lxml
config = {
'access_key': 'AKIAIKLBJZJSC65EHZAA',
'secret_key': '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',
'associate_tag': 'kdhua-20',
'locale': 'us'
}
def itemLookup(ASIN):
  api = amazonproduct.API(cfg=config)
  result = api.item_lookup(ASIN)
  for item in result.Items.items:
    print '%s (%s)' % (item.ItemAttributes.Title, item.ItemAttributes.Price)
    return item.ASIN
