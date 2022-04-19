from sklearn import pipeline


CRAWLER_NAME = "MITS"
CRAWLER_CONFIG = {
    "name" : "MITS", 
    "allowed_domains" : ['mgmits.ac.in'],
    "start_urls" : ['http://www.mgmits.ac.in/']
}
CRAWLER_SETTINGS = {
    "DEPTH_LIMIT":1,
    "LOG_LEVEL": "INFO",
    "IMAGE_STORE": "images",
    "ITEM_PIPELINES": {'scrapy.pipelines.images.ImagePipeline': 1}
}
CRAWLER_HTML_TAGS = ["p", "a"]


MONGODB_URI = "mongodb://localhost:27017"
MONOGODB_DATABASE = "Website_Chatbot"

