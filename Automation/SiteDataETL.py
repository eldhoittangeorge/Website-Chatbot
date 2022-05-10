import re 
import sys 
import pymongo
import logging
# import config
from configparser import ConfigParser
from pymongo import MongoClient

class DataETL:

    def __init__(self):

        self.config = ConfigParser()
        self.config.read("config.ini")
        self.client = MongoClient(self.config.get("Database", "mongodb_uri"))
        self.db= self.client[self.config.get("Database", "mongodb_database")]
        self.collection = self.db[self.config.get("Crawler", "crawler_name")]
        # self.client = MongoClient(config.MONGODB_URI)
        # self.client = MongoClient(config.MONGODB_URI)
        # self.db = self.client[config.MONOGODB_DATABASE]
        # self.collection = self.db[config.CRAWLER_NAME]

    def _clean_data(self, data):
        data = data.strip()
        data = re.sub("\xa0|\n|\|", "", data)
        return data.lower()


    def write_data_db(self, data):
        content = list(map(self._clean_data, data["data"])) 
        content = [x for x in content if x]
        content = " ".join(content)
        url = data["url"]

        if(sys.getsizeof(content) <= 3000):
            # logging.info("The data is here") 
            return
        
        document = {
            "source": url,
            "content": content
        }

        update = {
            "$set": {
                "source": url,
                "content": content
            }
        }


        self.collection.update_one(document, update=update, upsert=True)



    