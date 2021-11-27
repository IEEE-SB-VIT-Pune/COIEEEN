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
    return render_template('mine_block.html', data = mine_block())

@app.route('/get_chain', methods = ['GET'])
def get_chain_router():
    return render_template('get_chain.html', data = get_chain())

@app.route('/open_transactions', methods=['GET'])
def open_transactions_router():
    return render_template('open_transactions.html', data=blockchain.transactions)

@app.route('/is_valid', methods = ['GET'])
def is_valid_router():
    return render_template('is_valid.html', data=is_valid())

@app.route('/add_transaction', methods = ['GET', 'POST'])
def add_transaction_router():
    if request.method == "GET":
        return render_template("add_transaction.html")
    else:
        sender = request.form['sender']
        receiver = request.form['receiver']
        amount = request.form['amount']
        return add_transaction(sender, receiver, amount)

@app.route('/connect_node', methods = ['POST'])
def connect_node_router():
    return connect_node()

@app.route('/replace_chain', methods = ['GET'])
def replace_chain_router():
    return render_template('replace_chain.html', data=replace_chain())

if __name__ == "__main__":
    app.run()