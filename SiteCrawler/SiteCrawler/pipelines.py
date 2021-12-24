import re
from itemadapter import ItemAdapter


class SitecrawlerPipeline:

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
        with open(f"../Site Data/{file_name}.txt","w",encoding="utf-8") as fp:
        # with open(f"../Site Data/data.txt","a", encoding="utf-8") as fp:
            fp.write(item["url"]+"\n")
            fp.write(site_content)


    def process_item(self, item, spider):
        item["data"] = list(map(self.clean_data, item["data"]))
        item['data'] = list(filter(self.filter_data, item['data']))
        self.write_data(item)
        return item
