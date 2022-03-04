from flask import Flask, request,Response
from flask_cors import CORS
import pandas as pd
import re
from pymongo import MongoClient
# from src.ContextEvaluation import ContextEvalutaionClass
# from src.NonContexModel import NonContextModelClass
from src.Context import ContextModelClass 

app = Flask(__name__)
CORS(app)

context_evaluation_class = None
non_context_model = None
context_model = ContextModelClass()
url_to_file_mapping = None
# db_client = MongoClient(host="localhost", port=27017)
# database = db_client['Website_Chatbot']
# collection = database["MitsSpider"]

@app.before_first_request
def initialize_models():
    global context_evaluation_class
    global non_context_model
    # global context_model
    global url_to_file_mapping
    # context_evaluation_class = ContextEvalutaionClass()
    # non_context_model = NonContextModelClass()
    # context_model = ContextModelClass()

    url_to_file_mapping = pd.read_csv("src/file_to_url_mapping.csv")



def get_url_with_filename(filename):
    filename = re.sub(".txt", "", filename)
    tmp_rul = collection.find_one({})
    url = url_to_file_mapping[url_to_file_mapping.filename == filename]
    url = url["url"].values[0]
    if(url):
        return url
    else:
        return ""

@app.route("/api",methods=["POST","GET"])
def give_answer():
    query = request.args['query']
    # ans  = context_evaluation_class.predict(query)
    # ans = non_context_model.predict(query)
    results = context_model.predict(query)
    for result in results["answers"]:
        ans = result
        ans["source"] = str(get_url_with_filename(ans["document_link"]))
    return results 
