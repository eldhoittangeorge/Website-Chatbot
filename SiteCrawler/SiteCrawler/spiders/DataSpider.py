from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from SiteCrawler.items import SitecrawlerItem

class DataSpider(CrawlSpider):
    name = "MitsSpider"
    allowed_domains = ['mgmits.ac.in']
    start_urls = ["http://mgmits.ac.in/"]

    rules = (Rule(LinkExtractor(), callback="parse"),)


    def parse_home(self, response):
        self.logger.info("The parse home was called ")
        content = SitecrawlerItem()
        content['data'] = response.xpath('//p/text() | //h1/text() | //h2/text()').extract()
        content['url'] = response.url+"home"
        return content 

    def parse(self,response):
        content = SitecrawlerItem() 
        self.logger.info(f"The current crawling site is {response.url}")
        if(response.url == "http://mgmits.ac.in/"):
            yield self.parse_home(response)
        else:
            content["data"] = response.xpath('//p/text()[not(ancestor::*[@class="header" or @class = "footer-link-wrap" or @class="footer-wrap"])] | //h1/text() | //h2/text() | //li/text()').extract()
            content['url'] = response.url
            yield content
