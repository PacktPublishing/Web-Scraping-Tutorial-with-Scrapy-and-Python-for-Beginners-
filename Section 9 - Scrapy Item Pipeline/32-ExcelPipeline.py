from openpyxl import Workbook


class EbookScraperPipeline:

    # Called when spider is opened/started
    def open_spider(self, spider):
        # Creating an empty excel workbook/file
        self.workbook = Workbook()
        # Getting the first/active sheet
        self.sheet = self.workbook.active
        self.sheet.title = "ebooks"

        # Adding values to first rows
        self.sheet.append(spider.cols)

    # Given generated (yield) item from spider
    def process_item(self, item, spider):
        # Add the title & price value in a new row
        self.sheet.append([ item['title'], item['price'] ])
        return item

    # Called when spider is closed/finished
    def close_spider(self, spider):
        # Save the excel workbook/file
        self.workbook.save("ebooks.xlsx")
