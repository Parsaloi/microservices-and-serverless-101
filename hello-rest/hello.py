# hello.py
# import neccessary dependencines
from flask import Flask

# set app's entry point
app = Flask(__name__)

# explicit routing!!
@app.route("/")

# python method
def hello_rest():
    return "Hello REST API!"
