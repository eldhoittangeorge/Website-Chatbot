import scrapy


class SitecrawlerItem(scrapy.Item):
    data = scrapy.Field()
    # heading = scrapy.Field()