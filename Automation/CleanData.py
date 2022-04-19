from pkg_resources import cleanup_resources
import pymongo
from pymongo import MongoClient
import math
from collections import Counter
import config
import sys
import re


class CleanData:

    def __init__(self):
        self.db_client = MongoClient(config.MONGODB_URI)
        self.db = self.db_client[config.MONOGODB_DATABASE]
        self.collection = self.db[config.CRAWLER_NAME]
        self.contents = self._get_db_data()


    def _get_db_data(self):
        documents = []
        for item in self.collection.find():
            documents.append(item['content'])
        return documents

    def _extract_common(self, content):

        threshold = math.ceil(len(content) * .4)
        common_text = []
        i = 0
        while(True):
            tmp = [x[i] for x in content]
            status_lst = [x == tmp[0] for x in tmp]
            if(Counter(status_lst)[True] >= threshold):
                common_text.append(tmp[0])
                i = i + 1
            else:
                break

        return common_text

    def header_footer_cleaner(self):
        header_data = [x.split(" ") for x in self.contents]
        footer_data = [x[::-1] for x in header_data] 

        header_pattern = " ".join(self._extract_common(header_data))
        footer_pattern = " ".join(self._extract_common(footer_data)[::-1])

        cursor = self.collection.find()

        for document in cursor:
            id = document['_id']
            content = document["content"].replace(header_pattern, "", 1)
            content = content.replace(footer_pattern, "", 1).strip()

            if(sys.getsizeof(content) <= 1500):
                self.collection.delete_one({"_id":id})
                continue

            update = {
                "$set":{
                    "content": content 
                }
            }

            self.collection.update_one(document, update=update)


# clean_data = CleanData()
# clean_data.header_footer_cleaner()
