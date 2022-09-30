from scrapy_playwright.page import PageCoroutine
import scrapy


class OscarSpider(scrapy.Spider):
    name = 'oscar'

    def start_requests(self):
        yield scrapy.Request(
            "http://www.scrapethissite.com/pages/ajax-javascript/",
            meta={
                # enable playwright
                "playwright": True,
                # include the page object
                "playwright_include_page": True,
                # define the coroutines list, it can also be dict
                "playwright_page_coroutines": [
                    # click the given selector
                    PageCoroutine("click", "a#2015"),
                    # wait for the give selector to appear
                    PageCoroutine("wait_for_selector", "tr.film"),
                ]
            }
        )

    # Visit each page for year 2010 to 2015
    # def start_requests(self):
    #     for year in range(2010, 2016):
    #         yield scrapy.Request(
    #         "http://www.scrapethissite.com/pages/ajax-javascript/",
    #         meta={
    #             "playwright": True,
    #             "playwright_include_page": True,
    #             "playwright_page_coroutines": [
    #                 PageCoroutine("click", f"a#{year}"),
    #                 PageCoroutine("wait_for_selector", "tr.film"),
    #             ]
    #         }
    #     )
    #     or format the url

    async def parse(self, response):
        
        for row in response.css("tr.film"):
            yield {
                "title": row.css("td.film-title::text").get(),
                "awards": row.css("td.film-awards::text").get()
            }