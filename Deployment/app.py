from flask import Flask, request, render_template
from flask_cors import CORS
import ast 
from configparser import ConfigParser
from ContextModel import ContextModelClass 
# from ContextEvaluationModel import ContextEvaluationModel

app = Flask(__name__)
CORS(app)

context_model = ContextModelClass()

# Loading configration file
config = ConfigParser()
config.read("config.ini")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api",methods=["GET"])
def give_answer():
    query = request.args['query']
    results = context_model.predict(query)
    return results 
    # return {"ads":query}

@app.route("/config", methods=["GET"])
def get_config():
    name = config.get("Crawler", "crawler_name")
    website = ast.literal_eval(config.get("Crawler", "crawler_config"))["start_urls"][0]
    date = config.get("Date","date",fallback=None)
    response = {"name" :name, "website": website, "date": date}
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
