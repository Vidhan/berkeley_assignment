from flask import Flask
from flask import jsonify, current_app
from markupsafe import escape
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True



def instantiate_client():
    with open("secret.txt") as secret_file:
        uri = secret_file.readline()
        client = MongoClient(uri)
        db = client["berkeley"]
        collection = db["sediment_grain_size"]
    return collection

@app.route("/sampleid/<sample_id>")
def show_sample_id(sample_id):
    collection = instantiate_client()
    sample_id = escape(sample_id)
    data = collection.find_one({"Sample_ID": sample_id}, {"_id":0,"index":0})
    if data is None:
        return "Sample id is invalid"
    else:
        return data

@app.route("/")
def show_all_ids():
    collection = instantiate_client()
    data = list(collection.find({},{"_id":0,"Sample_ID":1}))
    if data is None:
        return "DB is empty"
    else:
        return data
