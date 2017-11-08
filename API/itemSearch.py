import amazonproduct
from amazonproduct import API
import lxml
def item_search(keywords, pctoff, searchIndex = 'All'):
  api = amazonproduct.API(cfg=~/.credential)
  result = api.item_search(searchIndex,Keywords=keywords, ResponseGroup='Large', MinPercentageOff=pctoff)
  total_results = result.results
  total_pages = len(result)  # or result.pages
  for items in result:
    print 'page %d of %d' % (result.current, total_pages)
    print items.ASIN + '\n'
    return items.ASIN
