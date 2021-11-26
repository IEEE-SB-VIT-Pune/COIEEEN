from flask import Flask, jsonify, request, render_template
import requests
from uuid import uuid4
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def default():
    return render_template('index.html')
