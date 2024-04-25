from flask import Flask, render_template, request,jsonify
import requests
from api_req import call_api
import os
import pdb
import json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    url = 'http://localhost:5071/api/Proposal/GetProposals'
    data = call_api(url)
    return render_template('index.html', data= data)

@app.route('/users',methods=['GET','POST'])
def users():
    proposalId = request.form['proposalId']
    url = 'http://localhost:5071/api/Proposal/GetUsers/'+proposalId
    data = call_api(url)
    return jsonify({'htmlresponse': render_template('users.html',data=data)})

if __name__ == "__main__":
    app.run(debug=True)