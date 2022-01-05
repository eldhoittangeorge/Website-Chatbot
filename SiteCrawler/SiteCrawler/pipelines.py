import pandas as pd
import re
from SiteCrawler.items import SitecrawlerTableItem, SitecrawlerItem

class SitecrawlerTablePipeline:

    def save_data(self, data):
        df = pd.DataFrame.from_records(data["table_data"], index=None)
        df = df[df.apply(lambda x: any(x.values != ""), axis=1)]
        if(df.size != 0):
            df.to_csv(f"../Site Data/Tables/{data['table_title']}.csv", index=False, header=False)


    def process_item(self, item, spider):
        if(isinstance(item, SitecrawlerTableItem)):
            self.save_data(item)
        return item


class SitecrawlerPipeline:

    def __init__(self):
        self.data = pd.DataFrame(columns=["data", "url"])

    def clean_data(self, data):
        data = data.strip()
        data = re.sub("\xa0|\n|\|","",data)
        return data

    def filter_data(self, data):
        return len(data) > 3

    def write_data(self, item):
        file_name = "mits_" + re.sub("https?://mgmits.ac.in/", "", item['url'])
        file_name = re.sub("/","_",file_name) 
        site_content = " ".join(item["data"])
        # self.data = self.data.append({"data" :site_content, "url":item["url"]}, ignore_index=True)


        with open(f"../Site Data/Data/{file_name}.txt","w+",encoding="utf-8") as fp:
        # with open(f"../Site Data/data.txt","a", encoding="utf-8") as fp:
            # fp.write(item["url"]+"\n")
            fp.write(site_content)

    # def close_spider(self, spider):
    #     self.data.to_csv("../Site Data/data.csv", index=False)


    def process_item(self, item, spider):
        if(isinstance(item, SitecrawlerItem)):
            item["data"] = list(map(self.clean_data, item["data"]))
            item['data'] = list(filter(self.filter_data, item['data']))
            self.write_data(item)
        return item
