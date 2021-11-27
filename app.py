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
    data = mine_block()
    print(data)
    return render_template('mine_block.html', data = data)

@app.route('/get_chain', methods = ['GET'])
def get_chain_router():
    return get_chain()

@app.route('/is_valid', methods = ['GET'])
def is_valid_router():
    return is_valid()

@app.route('/add_transaction', methods = ['GET', 'POST'])
def add_transaction_router():
    return add_transaction()

@app.route('/connect_node', methods = ['POST'])
def connect_node_router():
    return connect_node()

@app.route('/replace_chain', methods = ['GET'])
def replace_chain_router():
    return replace_chain()

if __name__ == "__main__":
    app.run()