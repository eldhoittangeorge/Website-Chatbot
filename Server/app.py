from flask import Flask, request,Response
from flask_cors import CORS
import pandas as pd
import re
from pymongo import MongoClient
from bson.objectid import ObjectId
# from src.ContextEvaluation import ContextEvalutaionClass
# from src.NonContexModel import NonContextModelClass
from src.Context import ContextModelClass 

app = Flask(__name__)
CORS(app)

context_evaluation_class = None
non_context_model = None
context_model = ContextModelClass()
url_to_file_mapping = None
db_client = MongoClient(host="localhost", port=27017)
database = db_client['Website_Chatbot']
collection = database["MitsSpider"]

# @app.before_first_request
# def initialize_models():
#     global context_evaluation_class
#     global non_context_model
#     # global context_model
#     global url_to_file_mapping
#     # context_evaluation_class = ContextEvalutaionClass()
#     # non_context_model = NonContextModelClass()
#     # context_model = ContextModelClass()

#     # url_to_file_mapping = pd.read_csv("src/file_to_url_mapping.csv")



def get_url(document_id):
    tmp_rul = collection.find_one({"_id":ObjectId(document_id)}, projection={"source":True})
    url = tmp_rul["source"]
    if(url):
        return url
    else:
        return ""

@app.route("/api",methods=["POST","GET"])
def give_answer():
    query = request.args['query']
    results = context_model.predict(query)
    for result in results["answers"]:
        ans = result
        ans["source"] = str(get_url(ans["document_id"]))
    return results 


#TODO if there is no link found return the home page from spider