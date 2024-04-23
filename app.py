from flask import Flask, render_template
import requests
from api_req import call_api
import os
import pdb
import json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    data = call_api()
    return render_template('index.html', data= data)