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
}
CRAWLER_HTML_TAGS = ["p"]


MONGODB_URI = "mongodb://localhost:27017"
MONOGODB_DATABASE = "Website_Chatbot"

