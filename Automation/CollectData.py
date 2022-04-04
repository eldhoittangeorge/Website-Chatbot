from py import process
import scrapy 
import re
import config
import logging
from SiteDataETL import DataETL
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor


class DataSpider(CrawlSpider):

    def __init__(self, *args, **kwargs):
        super(DataSpider, self).__init__(*args, **kwargs)
        self.data_etl = DataETL()


    name = config.CRAWLER_NAME 
    start_urls = config.CRAWLER_CONFIG["start_urls"]
    allowed_domains = config.CRAWLER_CONFIG["allowed_domains"]
    rules = (Rule(LinkExtractor(), callback="parse"),)


    def parse(self, response):
        data = response.xpath('//p/text() | //dd/text() | //b/text() | //a/text() | //li/text()').extract()
        url = response.url
        self.data_etl.write_data_db({"data" : data, "url" : url}) 
        yield {}



process = CrawlerProcess(settings={
    "DEPTH_LIMIT":1,
    "LOG_LEVEL" : "INFO"
})

process.crawl(DataSpider)
process.start()

