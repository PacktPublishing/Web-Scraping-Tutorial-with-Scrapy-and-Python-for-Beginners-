import json
import scrapy
from datetime import date


class TrackerSpider(scrapy.Spider):
    name = 'tracker'
    allowed_domains = ['amazon.com']
    
    def __init__(self, query="python for beginners", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base_url = "https://www.amazon.com"
        self.search_url = "https://www.amazon.com/s?k={query}"

        self.rank = None
        self.page_num = 1
        self.query = query

        self.start_urls = [self.search_url.format(
            query=query.replace(" ", "+")
        )]

    def parse(self, response):
        title = "Python 3.10: A Complete Guide Book To Python Programming For Beginners"
        title_v = title + " [Color Edition]"
        
        search_results: list = response.css("div.s-result-item "
                                      "h2 > a > span::text").getall()


        if title_v in search_results:
            page_pos = search_results.index(title_v)
            self.rank = ((self.page_num - 1) * 48) + page_pos

        else:
            # not found
            next_btn = response.css("a.s-pagination-next")
            
            if next_btn:
                self.page_num += 1

                yield scrapy.Request(
                    self.base_url + next_btn.attrib["href"]
                )
            else:
                self.rank = "Not found!"
        
        self.export()

    def export(self):
        today = date.today().strftime("%d-%M-%Y")

        with open("track.json") as file:
            dt = json.load(file)

        if self.query in dt:
            dt[self.query][today] = self.rank
        else:
            dt[self.query] = {
                today: self.rank
            }

        with open("track.json", "w") as file:
            json.dump(dt, file)