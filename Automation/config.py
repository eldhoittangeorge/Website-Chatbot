CRAWLER_NAME = "MITS"
CRAWLER_CONFIG = {
    "name" : "MITS", 
    "allowed_domains" : ['mgmits.ac.in'],
    "start_urls" : ['http://mgmits.ac.in']
}

CRAWLER_SETTINGS = {
    "DEPTH_LIMIT":1,
    "LOG_LEVEL": "INFO"
}

MONGODB_URI = "mongodb://localhost:27017"
MONOGODB_DATABASE = "Website_Chatbot"

