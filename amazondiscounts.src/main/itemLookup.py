# from past import autotranslate
# autotranslate(['amazonproduct'])
import amazonproduct

config = {
    'access_key': 'AKIAIKLBJZJSC65EHZAA',
    'secret_key': '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',
    'associate_tag': 'kdhua-20',
    'locale': 'us'
}

# input: Asin
# output: [title, price, URL]
def item_lookup(asin):
    api = amazonproduct.API(cfg=config)
    result = api.item_lookup(asin, ResponseGroup= 'Large')
    titlePriceURLList = []
    item = result.Items.Item
    titlePriceURLList.append(item.ItemAttributes.Title)
    titlePriceURLList.append(item.OfferSummary.LowestNewPrice.FormattedPrice)
    titlePriceURLList.append(item.DetailPageURL)
    return titlePriceURLList
