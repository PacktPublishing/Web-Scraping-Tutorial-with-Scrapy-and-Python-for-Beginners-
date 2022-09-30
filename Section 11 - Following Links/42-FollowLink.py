import scrapy
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader


class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = [ "https://books.toscrape.com/catalogue/category/books/travel_2/" ]

    def parse(self, response):
        # getting all the article elements
        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            # extracting the details page url
            url = ebook.css("h3 a").attrib["href"]
            # sending a request to the details page
            yield scrapy.Request(
                url = self.start_urls[0] + url,
                callback = self.parse_details
            )

    def parse_details(self, response):
        main = response.css("div.product_main")
        # initialize the itemloader with selector
        loader = ItemLoader(item=EbookItem(), selector=main)

        loader.add_css("title", "h1::text")
        loader.add_css("price", "p.price_color::text")
        # selecting the quantity data with regular expression
        quantity_p = main.css("p.availability")
        loader.add_value(
            "quantity", 
            quantity_p.re(r'\(.+ available\)')[0]
            # Regular Expressions used:
            # \ - escape character or treat 
            #     as normal character.
            # . - any character (a-Z, 0-9, $, %, etc.)
            # + - one or more characters
        )

        yield loader.load_item()