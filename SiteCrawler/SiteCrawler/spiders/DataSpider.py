from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from SiteCrawler.items import SitecrawlerItem,SitecrawlerTableItem

class DataSpider(CrawlSpider):
    name = "MitsSpider"
    allowed_domains = ['mgmits.ac.in']
    start_urls = ["http://mgmits.ac.in/"]

    rules = (Rule(LinkExtractor(), callback="parse"),)

    def parse_home(self, response):
        content = SitecrawlerItem()
        content['data'] = response.xpath('//p/text() | //h1/text() | //h2/text()').extract()
        content['url'] = response.url+"home"
        return content 


    def html_filter(self, css_class): 
       return css_class != "follow-us-on"

    def parse_table(self, response):
        site_table_item = SitecrawlerTableItem()
        soup = BeautifulSoup(response.text, "lxml")
        title = soup.find("span", class_="has-vivid-red-color")
        title = title.get_text() if (title != None) else soup.find("h2").get_text() 
        table = soup.find("table", class_= self.html_filter)
        table_df = list() 
        if(not table):
            return None
        for row in table.findAll("tr"):
            cells = row.findAll("td")
            temp_row = list()
            for cell in cells:
                temp_row.append(cell.get_text())
            table_df.append(temp_row)
        site_table_item["table_data"] = table_df
        site_table_item["table_title"] = title
        return site_table_item


    def parse(self,response):
        content = SitecrawlerItem() 
        if(response.url == "http://mgmits.ac.in/"):
            yield self.parse_home(response)
        else:
            table_content = response.xpath("//table")
            if(table_content):
                yield self.parse_table(response)
            content["data"] = response.xpath('//p/text()[not(ancestor::*[@class="header" or @class = "footer-link-wrap" or @class="footer-wrap"])] | //h1/text() | //h2/text() | //li/text()').extract()
            content['url'] = response.url
            yield content
