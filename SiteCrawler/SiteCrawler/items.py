import scrapy


class SitecrawlerItem(scrapy.Item):
    data = scrapy.Field()
    url = scrapy.Field()
    # heading = scrapy.Field()

# class SitecrawlerTableItem(scrapy.Item):
#     key = scrapy.Field()
#     value = scrapy.Field()