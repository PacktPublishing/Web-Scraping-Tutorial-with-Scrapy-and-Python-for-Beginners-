import scrapy
from scrapy.loader import ItemLoader
from ebook_scraper.items import EbookItem

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = [ "https://books.toscrape.com/catalogue/category/books/travel_2" ]

    def __init__(self):
        super().__init__()
        # intial page count
        self.page_count = 0

    def parse(self, response):
        # increment page count
        self.page_count += 1
        # select all the article elements
        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            # intialize the itemloader with selector
            loader = ItemLoader(item=EbookItem(), selector=ebook)

            loader.add_css('title', "h3 a::attr(title)")
            loader.add_css('price', "p.price_color::text")

            yield loader.load_item()

        print("[ PAGE COUNT ]:", self.page_count)

        # select the next page
        next_btn = response.css("li.next a")
        # check for the next page
        if next_btn:
            # send a request to the next page
            next_page = f"{self.start_urls[0]}/{next_btn.attrib['href']}"
            yield scrapy.Request(url=next_page)