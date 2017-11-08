import amazonproduct
from amazonproduct import API
import lxml
def itemLookup(ASIN):
  api = amazonproduct.API(cfg=~/.credential)
  result = api.item_lookup(ASIN)
  for item in result.Items.items:
    print '%s (%s)' % (item.ItemAttributes.Title, item.ItemAttributes.Price)
    return item.ASIN
