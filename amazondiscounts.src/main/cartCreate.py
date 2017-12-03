import amazonproduct
from amazonproduct import API
import lxml
config = {
  'access_key': 'AKIAIKLBJZJSC65EHZAA',
  'secret_key': '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',
  'associate_tag': 'kdhua-20',
  'locale': 'us'
}

def cartCreate(asin):
  api = amazonproduct.API(cfg=config)
  result = api.item_lookup(asin, ResponseGroup= 'Large')
  for item in result.Items.Item:
     offer_id = item.Offers.Offer.OfferListing.OfferListingId
     Items = {
         'Item.1.OfferListingId': offer_id,
         'Item.1.Quantity': 1
     }
     #TODO: create a virtual cart with cart_create()
     cart = api.cart_create(Items=data, Quantity=1)
     cart = api.cart_create('OfferListingId=item.Offers.Offer.OfferListing.OfferListingId, Quantity=1')
     # the above code doesn't work
     break

# test: should get OfferListingId and create a cart with a seat cushion in it 
cartCreate('B00V2L5JRA')
