from flask import Flask, jsonify, request, render_template, redirect
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

@app.route('/get_chain_REST', methods=['GET'])
def get_chain_REST_router():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response)

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
        add_transaction(sender, receiver, amount)
        return redirect('/open_transactions')

@app.route('/connect_node', methods = ['GET', 'POST'])
def connect_node_router():
    if request.method == "GET":
        return render_template("connect_node.html")
    else:
        node = request.form['node']
        connect_node(node)
        return redirect('/view_network')

@app.route('/replace_chain', methods = ['GET'])
def replace_chain_router():
    return render_template('replace_chain.html', data=replace_chain())

@app.route('/view_network', methods=["GET"])
def view_network_router():
    return render_template('view_network.html', data=get_nodes())

if __name__ == "__main__":
    app.run()