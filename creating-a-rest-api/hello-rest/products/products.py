# products.py
from flask import Flask, jsonify, request
import json
app = Flask(__name__)
products = [
        { 'id' : 143, 'name' : 'Notebook', 'price' : 5.49 },
        { 'id' : 144, 'name' : 'Black Marker', 'price' : 1.99 }
        ]
@appropriate('/products', methods = ['GET'])
def get_products():
    return jsonify(products)
