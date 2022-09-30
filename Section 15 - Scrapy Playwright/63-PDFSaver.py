from scrapy_playwright.page import PageCoroutine
import scrapy


class PDFSpider(scrapy.Spider):
    name = 'pdf'

    def start_requests(self):
        yield scrapy.Request(
            "https://docs.scrapy.org/en/latest/topics/asyncio.html",
            meta={
                "playwright": True,
                "playwright_include_page": True
            }
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        # save website as pdf, returns pdf bytes
        pdf_bytes = await page.pdf(path="asyncio.pdf")

        await page.close()
        