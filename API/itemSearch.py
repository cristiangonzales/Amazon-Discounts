import amazonproduct
from amazonproduct import API
import lxml
def itemSearch(keywords, pctoff, searchIndex = 'All'):
    api = amazonproduct.API(cfg=~/.credential)
    result = api.item_search(searchIndex,Keywords=keywords, ResponseGroup='Large', MinPercentageOff=pctoff)
    asin_list = []
    for item in result:
      asin_list.append(item.ASIN)
      print (item.DetailPageURL)
    return asin_list

def main():
    asin_results = itemSearch('chair', 50)
    for item in asin_results:
      print item

if __name__ == '__main__':
  main()
  
