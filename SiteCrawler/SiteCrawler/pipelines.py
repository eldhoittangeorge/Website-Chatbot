from pydoc import doc
import pandas as pd
import logging
import sys
import re
import os
import pymongo
from pymongo import MongoClient
from SiteCrawler.items import  SitecrawlerItem

class SitecrawlerPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    def clean_data(self, data):
        data = data.strip()
        data = re.sub("\xa0|\n|\|", "", data)
        return data

    def filter_data(self, data):
        return len(data) > 10 

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get("MONGODB_URI"),
            mongo_db = crawler.settings.get("MONGODB_DATABASE")
        )

    def open_spider(self, spider):
        pass
        # self.client = MongoClient(self.mongo_uri)
        # self.db = self.client[self.mongo_db]
        # self.collection = self.db[spider.name]
        # self.collection.create_index([('source',pymongo.ASCENDING),
        # ('content',pymongo.ASCENDING)], unique=True)

    def write_data(self, item, spider_name):
        # self.write_data_file(item)
        pass
        # source = item["url"]
        # content = " ".join(item["data"])
        # document = {
        #     "source" : source,
        #     "content" : content
        # }
        # update = {
        #     "$set":{
        #         "source": source,
        #         "content": content
        #     }
        # }
        # self.collection.update_one(document, update=update, upsert=True)

    def write_data_file(self, item):
        file_name = "op_"+re.sub("https://onepiece.fandom.com","", item['url'])
        file_name = re.sub("/", "_", file_name)
        site_content = " ".join(item['data'])


        if(sys.getsizeof(site_content) > 3000):
            with open(f"../../Site Data/Data/{file_name}.txt", "w+",encoding="utf-8") as fp:
                fp.write(site_content)

    
    def close_spider(self, spider):
            self.client.close()


    def process_item(self, item, spider):
        if(isinstance(item, SitecrawlerItem)):
            item["data"] = list(map(self.clean_data, item["data"]))
            item['data'] = list(filter(self.filter_data, item['data']))
            logging.info(item['url'])
            self.write_data(item, spider.name)
        return item
