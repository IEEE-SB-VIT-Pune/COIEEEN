from flask import Flask, jsonify, request, render_template
import requests
from uuid import uuid4
from urllib.parse import urlparse
from blockchain import Blockchain

from controllers.blockchain import *

# Create Flask app
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def default():
    return render_template('index.html')

@app.route('/mine_block', methods=['GET'])
def mine_block_router():
    return mine_block()
