from pydoc import doc
import pandas as pd
import logging
import re
import os
import pymongo
from pymongo import MongoClient
from SiteCrawler.items import SitecrawlerTableItem, SitecrawlerItem

class SitecrawlerTablePipeline:

    def save_data(self, data):
        pass
        # df = pd.DataFrame.from_records(data["table_data"], index=None)
        # df = df[df.apply(lambda x: any(x.values != ""), axis=1)]
        # if(df.size != 0):
        #     df.to_csv(f"../../../Site Data/Tables/{data['table_title']}.csv", index=False, header=False)


    def process_item(self, item, spider):
        pass
        # if(isinstance(item, SitecrawlerTableItem)):
        #     self.save_data(item)
        # return item


class SitecrawlerPipeline:

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    def clean_data(self, data):
        data = data.strip()
        data = re.sub("\xa0|\n|\|","",data)
        return data

    def filter_data(self, data):
        return len(data) > 3

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get("MONGODB_URI"),
            mongo_db = crawler.settings.get("MONGODB_DATABASE")
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[spider.name]
        self.collection.create_index([('source',pymongo.ASCENDING),
        ('content',pymongo.ASCENDING)], unique=True)

    def write_data(self, item, spider_name):
        source = item["url"]
        content = " ".join(item["data"])
        document = {
            "source" : source,
            "content" : content
        }
        update = {
            "$set":{
                "source": source,
                "content": content
            }
        }
        self.collection.update_one(document, update=update, upsert=True)

    def close_spider(self, spider):
            self.client.close()


    def process_item(self, item, spider):
        if(isinstance(item, SitecrawlerItem)):
            item["data"] = list(map(self.clean_data, item["data"]))
            item['data'] = list(filter(self.filter_data, item['data']))
            self.write_data(item, spider.name)
        return item
