from scrapy_playwright.page import PageCoroutine
import scrapy


class ScreenshotSpider(scrapy.Spider):
    name = 'snip'

    def start_requests(self):
        yield scrapy.Request(
            "https://unsplash.com/",
            meta={
                "playwright": True,
                "playwright_include_page": True
            }
        )

    async def parse(self, response):
        # get playwright page object
        page = response.meta["playwright_page"]
        # take a screenshot of the web and save it
        await page.screenshot(path="snip.png", full_page=True)
        # close the website
        await page.close()