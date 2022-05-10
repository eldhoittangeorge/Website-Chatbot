import datetime
import ast
from configparser import ConfigParser
from scrapy.crawler import CrawlerProcess
from CollectData import DataSpider
from CreateModel import ModelCreator
from CleanData import CleanData

class Main():

    def __init__(self):
        self.config = ConfigParser()
        self.config.read("config.ini")
        self.crawler = self.initialize_crawler()


    def initialize_crawler(self):
        settings = ast.literal_eval(self.config.get("Crawler", "crawler_settings"))
        crawler_process = CrawlerProcess(settings=settings)
        return crawler_process

    def write_date_to_config(self, date):
        if(self.config.has_section("Date")):
            self.config.set("Date", "date", str(date))
        else:
            self.config["Date"] = {"date": str(date)}        

        with open("config.ini", "w") as config_fp:
            self.config.write(config_fp)


    def start(self):
        self.crawler.crawl(DataSpider)
        self.crawler.start()
        self.write_date_to_config(datetime.date.today())
        print("Data collection ended")
        
        print("Data Cleaning started")
        data_cleaner = CleanData()
        data_cleaner.header_footer_cleaner()
        print("Data Cleaning ended")

        model_creator = ModelCreator()
        model_creator.create_and_save()

if __name__ == '__main__':
    main = Main()
    main.start()
