from py import process
import scrapy 
import config
from SiteDataETL import DataETL
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor


class DataSpider(CrawlSpider):

    def __init__(self, *args, **kwargs):
        print("Collect data started")
        super(DataSpider, self).__init__(*args, **kwargs)
        self.data_etl = DataETL()
        self.xpath_tag = self._create_crawler_tags()


    name = config.CRAWLER_NAME 
    start_urls = config.CRAWLER_CONFIG["start_urls"]
    allowed_domains = config.CRAWLER_CONFIG["allowed_domains"]
    rules = (Rule(LinkExtractor(), callback="parse"),)


    def _create_crawler_tags(self):
        xpath_tag = ""
        for tag in config.CRAWLER_HTML_TAGS:
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

