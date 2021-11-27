from flask import jsonify, request
import json
import hashlib
from uuid import uuid4

from blockchain import Blockchain

blockchain = Blockchain()

node_address = str(uuid4()).replace('-', '')

def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']

    proof = blockchain.proof_of_work(previous_proof)

    previous_hash = previous_block['block_hash']

    block_hash = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()


    blockchain.add_transaction(sender = node_address, receiver = 'You', amount = 1)
    block = blockchain.create_block(proof, previous_hash, block_hash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'block_hash': block['block_hash'],
                'transactions': block['transactions']}
    return response

def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return response

def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return response

def add_transaction():
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in json for key in transaction_keys):
        return 'Some elements of the transaction are missing'
    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    response = {'message': f'This transaction will be added to Block {index}'}
    return response

def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return "No node"
    for node in nodes:
        blockchain.add_node(node)
    response = {'message': 'All the nodes are now connected. The Hadcoin Blockchain now contains the following nodes:',
                'total_nodes': list(blockchain.nodes)}
    return response

def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'The nodes had different chains so the chain was replaced by the longest one.',
                    'chain': blockchain.chain}
    else:
        response = {'message': 'All good. The chain is the largest one.',
                    'chain': blockchain.chain}
    return response

