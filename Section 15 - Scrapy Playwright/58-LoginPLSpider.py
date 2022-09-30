from scrapy.selector import Selector
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'

    def start_requests(self):
        # send request with playwright enabled
        yield scrapy.Request(
            "https://www.stealmylogin.com/demo.html",
            meta={
                "playwright": True,
                "playwright_include_page": True 
            }
        )

    async def parse(self, response):
        # get the playwright page object
        page = response.meta["playwright_page"]

        # fill in the form fields
        await page.fill("input[name=username]", "random")
        await page.fill("input[name=password]", "random")
        # click on the submit button
        # 👇 will make sure you wait for the page to reload
        await page.click("input[type=submit]")
        # get the inner html/content of a selector
        html_content = await page.inner_html("body")

        await page.close()
        
        body = Selector(text=html_content) 
        yield {
            "heading": body.css("h1::text").get(),
            "paragraph": body.css("p::text").get()
        }
        

