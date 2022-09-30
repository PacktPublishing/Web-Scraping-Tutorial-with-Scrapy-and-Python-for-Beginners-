import scrapy


class EbookSpider(scrapy.Spider):
    # spider name
    name = 'ebook'
    # urls to request for
    start_urls = 'https://books.toscrape.com/'

    # recieve the response of the above request
    def parse(self, response):
        # select all the article elements
        # with ebook data using css selector
        ebooks = response.css("article")

        for ebook in ebooks:
            # extract each ebook's title and price
            title = ebook.css("a::text").get()
            price = ebook.css("p.price_color::text").get()

            # yield/generate the output for scrapy
            # to catch and extract to a different
            # file (, if specified)
            yield {
                "title": title, "price": price
            }