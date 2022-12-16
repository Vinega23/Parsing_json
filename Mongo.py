import pymongo
from pymongo import MongoClient
import json

cluster = MongoClient("mongodb+srv://Vinega:1234@cluster0.y5ijfbf.mongodb.net/?retryWrites=true&w=majority")
db = cluster["teska"]
collection = db["teska"]

with open('result-data.json') as f:
    data_res = json.load(f)

post = data_res
collection.insert_many(post)
