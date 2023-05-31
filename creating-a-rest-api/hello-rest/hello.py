# hello.py
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_rest():
    return "Hello REST API!"
