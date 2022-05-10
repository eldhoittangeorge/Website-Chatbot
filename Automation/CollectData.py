import scrapy 
# import config
import ast
from configparser import ConfigParser
from SiteDataETL import DataETL
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor


class DataSpider(CrawlSpider):

    config = ConfigParser()
    config.read("config.ini")

    def __init__(self, *args, **kwargs):
        print("Collect data started")
        super(DataSpider, self).__init__(*args, **kwargs)
        self.data_etl = DataETL()
        self.xpath_tag = self._create_crawler_tags()


    
    name = config.get("Crawler","crawler_name")
    start_urls = ast.literal_eval(config.get("Crawler", "crawler_config"))["start_urls"]
    allowed_domains = ast.literal_eval(config.get("Crawler", "crawler_config"))["allowed_domains"]
    rules = (Rule(LinkExtractor(), callback="parse"),)


    def _create_crawler_tags(self):
        xpath_tag = ""
        tags = ast.literal_eval(self.config.get("Crawler","crawler_html_tag"))
        for tag in tags:
            xpath_tag += f" //{tag}/text() |"
        xpath_tag = xpath_tag[1:-1]
        return xpath_tag

    def parse(self, response):
        data = response.xpath(self.xpath_tag).extract()
        # rel_img_ulrs = response.xpath("//img/@src").extract()
        url = response.url
        self.data_etl.write_data_db({"data" : data, "url" : url}) 
        yield {}



# process = CrawlerProcess(settings={
#     "DEPTH_LIMIT":1,
#     "LOG_LEVEL" : "INFO"
# })

# process.crawl(DataSpider)
# process.start()

