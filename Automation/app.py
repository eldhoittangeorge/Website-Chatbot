from urllib import response
from flask import Flask, request
from flask_cors import CORS
import pandas as pd
import config
from pymongo import MongoClient
from bson.objectid import ObjectId
from ContextModel import ContextModelClass 

app = Flask(__name__)
CORS(app)

context_model = ContextModelClass()
url_to_file_mapping = None
db_client = MongoClient(config.MONGODB_URI)
database = db_client[config.MONOGODB_DATABASE]
collection = database[config.CRAWLER_NAME]



def get_url(document_id):
    tmp_rul = collection.find_one({"_id":ObjectId(document_id)}, projection={"source":True})
    url = tmp_rul["source"]
    if(url):
        return url
    else:
        return ""

@app.route("/api",methods=["GET"])
def give_answer():
    query = request.args['query']
    results = context_model.predict(query)
    for result in results["answers"]:
        ans = result
        ans["source"] = str(get_url(ans["document_id"]))
    return results 

@app.route("/config", methods=["GET"])
def get_config():
    response = {"name" :config.CRAWLER_NAME, "website":config.CRAWLER_CONFIG["start_urls"][0]}
    return response




if __name__ == '__main__':
    app.run(host="localhost", debug=True)
