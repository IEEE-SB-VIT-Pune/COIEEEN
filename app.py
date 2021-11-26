from flask import Flask, jsonify, request, render_template
import requests
from uuid import uuid4
from urllib.parse import urlparse
from blockchain import Blockchain
# Create Flask app
app = Flask(__name__)

# Instantiate an object from the blockchain class
blockchain = Blockchain()

@app.route('/', methods = ['GET'])
def default():
    return render_template('index.html')
