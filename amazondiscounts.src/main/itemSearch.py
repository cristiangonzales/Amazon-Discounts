# from past import autotranslate
# autotranslate(['amazonproduct'])
import amazonproduct

config = {
'access_key': 'AKIAIKLBJZJSC65EHZAA',
'secret_key': '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',
'associate_tag': 'kdhua-20',
'locale': 'us'
}
def item_search(keywords, pctoff, searchIndex = 'All'):
    api = amazonproduct.API(cfg=config)
    result = api.item_search(searchIndex,Keywords=keywords, ResponseGroup='Large', MinPercentageOff=pctoff)
    asinList = []
    for item in result:
        asinList.append(item.ASIN)
    return asinList
