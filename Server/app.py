from flask import Flask, request,Response
from flask_cors import CORS
from src.ContextEvaluation import ContextEvalutaionClass
from src.NonContexModel import NonContextModelClass
from src.Context import ContextModelClass 

app = Flask(__name__)
CORS(app)

context_evaluation_class = None
non_context_model = None
context_model = None

@app.before_first_request
def initialize_models():
    global context_evaluation_class
    global non_context_model
    global context_model
    # context_evaluation_class = ContextEvalutaionClass()
    # non_context_model = NonContextModelClass()
    context_model = ContextModelClass()



@app.route("/api",methods=["POST","GET"])
def test():
    query = request.args['query']
    # ans = non_context_model.predict(query)
    ans = context_model.predict(query)
    return ans 
