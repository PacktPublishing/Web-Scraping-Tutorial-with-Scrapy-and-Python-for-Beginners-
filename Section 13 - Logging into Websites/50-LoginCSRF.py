import scrapy


class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = [ "http://www.scrapethissite.com/pages/advanced/?gotcha=csrf" ]

    # First request to log in
    def parse(self, response):
        # extract CSRF value
        csrf_token = response.css("input[name='csrf']").attrib["value"]
        print("[ CSRF ]:", csrf_token)

        # send FormRequest with csrf
        yield scrapy.FormRequest(
            "http://www.scrapethissite.com/pages/advanced/?gotcha=csrf",
            formdata={
                "user": "john",
                "pass": "__strong__",
                "csrf": csrf_token
            },
            callback=self.parse_login
        )

    # Parse logged in data
    def parse_login(self, response):
        print("[ Result ]:", response.css("div.row div::text").get().strip())