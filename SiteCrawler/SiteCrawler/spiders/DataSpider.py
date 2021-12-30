from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from SiteCrawler.items import SitecrawlerItem

class DataSpider(Spider):
    name = "MitsSpider"
    allowed_domains = ['mgmits.ac.in']
    # start_urls = ["http://mgmits.ac.in/"]
    start_urls = ["http://mgmits.ac.in/infrastructure/hostel/"]

    # rules = (Rule(LinkExtractor(), callback="parse"),)


    def parse_home(self, response):
        self.logger.info("The parse home was called ")
        content = SitecrawlerItem()
        content['data'] = response.xpath('//p/text() | //h1/text() | //h2/text()').extract()
        content['url'] = response.url+"home"
        return content 

    def parse_table(self, response):
        self.logger.info("A table was found")
        table = response.xpath("//table").extract()
        self.logger.info(table) 
        return None



    def parse(self,response):
        content = SitecrawlerItem() 
        if(response.url == "http://mgmits.ac.in/"):
            yield self.parse_home(response)
        elif(response.xpath("//table")):
            yield self.parse_table(response)
        else:
            content["data"] = response.xpath('//p/text()[not(ancestor::*[@class="header" or @class = "footer-link-wrap" or @class="footer-wrap"])] | //h1/text() | //h2/text() | //li/text()').extract()
            content['url'] = response.url
            # self.logger.info(content)
            yield content
