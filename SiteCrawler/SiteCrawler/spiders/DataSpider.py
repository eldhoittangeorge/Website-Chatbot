from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from SiteCrawler.items import SitecrawlerItem

class DataSpider(Spider):
    name = "MitsSpider"
    allowed_domains = ['mgmits.ac.in']
    start_urls = ["http://mgmits.ac.in/"]

    # rules = (Rule(LinkExtractor(), callback="parse"), )

    def parse(self,response):
        content = SitecrawlerItem() 
        content["data"] = response.xpath('//p/text() | //h1/text() | //h2/text()').extract()
        yield content
