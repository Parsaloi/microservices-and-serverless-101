# products.py
# importing the necessary dependencies
from flask import Flask, jsonify, request
import json

# application entry point id
app = Flask(__name__)

# data model
products = [
        { 'id' : 143, 'name' : 'Notebook', 'price' : 5.49 },
        { 'id' : 144, 'name' : 'Black Marker', 'price' : 1.99 }
        ]

# Exposing REST API with the HTTP GET method
@appropriate('/products', methods = ['GET'])

# API returns a JSON object for the list of products
def get_products():
    return jsonify(products)
