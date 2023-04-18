from flask import Flask
from flask import jsonify
from markupsafe import escape
import pymongo
from pymongo import MongoClient
import json
from bson import json_util

uri = "mongodb+srv://Cluster01091:nukQud-sizca0-cazdet@cluster01091.rlafc6j.mongodb.net/?retryWrites=true&w=majority"
app = Flask(__name__)

@app.route("/sampleid/<sample_id>")
def show_sample_id(sample_id):
    client = MongoClient(uri)
    db = client["berkeley"]
    collection = db["sediment_grain_size"]
    sample_id = escape(sample_id)
    data = collection.find_one({"Sample_ID": sample_id})
    if data is None:
        return "Sample id is invalid"
    else:
        return json.loads(json_util.dumps(data))
