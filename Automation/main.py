from dataclasses import dataclass
import config
from scrapy.crawler import CrawlerProcess
from CollectData import DataSpider
from CreateModel import ModelCreator
from CleanData import CleanData

class Main():

    def __init__(self):
        self.crawler = self.initialize_crawler()


    def initialize_crawler(self):
        crawler_process = CrawlerProcess(settings=config.CRAWLER_SETTINGS)
        return crawler_process


    def start(self):
        self.crawler.crawl(DataSpider)
        self.crawler.start()
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
