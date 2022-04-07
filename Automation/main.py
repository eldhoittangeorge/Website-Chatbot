import config
from scrapy.crawler import CrawlerProcess
from CollectData import DataSpider
from CreateModel import ModelCreator

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

        model_creator = ModelCreator()
        model_creator.create_and_save()

if __name__ == '__main__':
    main = Main()
    main.start()
