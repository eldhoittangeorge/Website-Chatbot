import re
from itemadapter import ItemAdapter


class SitecrawlerPipeline:

    # def clean_data(data):
    #     data = re.sub("\xa0|\||\s","",data)
    #     return data 


    def process_item(self, item, spider):
        item['data'] = list(map(lambda x :re.sub("\xa0|\n|\|","",x),item['data']))
        item['data'] = list(filter(lambda x : len(x) > 3,item['data']))
        return item
