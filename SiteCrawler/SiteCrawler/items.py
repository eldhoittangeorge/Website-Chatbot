import scrapy


class SitecrawlerItem(scrapy.Item):
    data = scrapy.Field()
    url = scrapy.Field()
    # heading = scrapy.Field()

class SitecrawlerTableItem(scrapy.Item):
    table_data = scrapy.Field()
    table_title = scrapy.Field()