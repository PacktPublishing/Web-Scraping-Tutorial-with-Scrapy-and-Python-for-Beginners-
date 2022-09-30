import scrapy


class EbookSpider(scrapy.Spider):
    name = "ebook"
    # start_urls = [ "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html" ]

    def start_requests(self):
        yield scrapy.FormRequest(
            "http://www.scrapethissite.com/pages/advanced/?gotcha=login",
            formdata={
                "user": "kyle",
                "pass": "really_strong"
            }
        )

    def parse(self, response):
        print(
            "[ Result ]:",
            response.css("div.container div div::text").get()
        )