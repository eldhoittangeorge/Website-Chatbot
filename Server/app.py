from flask import Flask, request

app = Flask(__name__)

@app.route("/api",methods=["POST"])
def test():
    return f"Hello, World! {request.form['one']}" 