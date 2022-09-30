from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst


def get_price(txt):
    return float(txt.replace('£', '' ))

def get_quantity(txt):
    # takes txt as '(19 available)' pattern
    # and returns 19 from the pattern
    return int(
        txt.replace('(', '').split()[0]
    )

class EbookItem(Item):
    title = Field(
        output_processor=TakeFirst()
    )
    price = Field(
        input_processor=MapCompose(get_price),
        output_processor=TakeFirst()
    )
    quantity = Field(
        input_processor=MapCompose(get_quantity),
        output_processor=TakeFirst()
    )