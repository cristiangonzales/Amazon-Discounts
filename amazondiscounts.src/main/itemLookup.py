from past import autotranslate
autotranslate(['amazonproduct'])
import amazonproduct
import time
config = {
    'access_key': 'AKIAIKLBJZJSC65EHZAA',
    'secret_key': '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',
    'associate_tag': 'kdhua-20',
    'locale': 'us'
}

# input: Asin
# output: [title, price, URL]
def item_lookup(asin):
    time.sleep(1)
    try:
        api = amazonproduct.API(cfg=config)
        result = api.item_lookup(asin, ResponseGroup= 'Large')
        titlePriceURLList = []
        item = result.Items.Item
        titlePriceURLList.append(str(item.ItemAttributes.Title))
        price = str(item.OfferSummary.LowestNewPrice.FormattedPrice).replace('$', '')
        titlePriceURLList.append(price)
        titlePriceURLList.append(str(item.DetailPageURL))
        return titlePriceURLList
    except:
        return ['Except','Except','Except']