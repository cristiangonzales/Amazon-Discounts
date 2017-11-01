import amazonproduct
from amazonproduct import API
import lxml
config = {
'access_key': 'AKIAIKLBJZJSC65EHZAA',
'secret_key': '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',
'associate_tag': 'kdhua-20',
'locale': 'us'
}
api = amazonproduct.API(cfg=config)

result = api.item_search('All',Keywords='chair', ResponseGroup='Large')

    # extract paging information
total_results = result.results
total_pages = len(result)  # or result.pages

for chairs in result:

    print 'page %d of %d' % (result.current, total_pages)
    print chairs.ASIN + '\n'

   