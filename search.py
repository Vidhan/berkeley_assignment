from flask import Flask
from flask import jsonify, current_app
from markupsafe import escape
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

with open("secret.txt") as secret_file:
    uri = secret_file.readline()

@app.route("/sampleid/<sample_id>")
def show_sample_id(sample_id):
    client = MongoClient(uri)
    db = client["berkeley"]
    collection = db["sediment_grain_size"]
    sample_id = escape(sample_id)
    data = collection.find_one({"Sample_ID": sample_id}, {"_id":0,"index":0})
    if data is None:
        return "Sample id is invalid"
    else:
        return data

@app.route("/")
def show_all_ids():
    client = MongoClient(uri)
    db = client["berkeley"]
    collection = db["sediment_grain_size"]
    data = list(collection.find({},{"_id":0,"Sample_ID":1}))
    if data is None:
        return "DB is empty"
    else:
        return data
