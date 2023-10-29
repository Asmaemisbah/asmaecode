

from unicodedata import name

from flask import Flask, render_template , url_for,session,redirect,request,Response
from pymongo import MongoClient
from datetime import datetime
from simple_detect import SimpleDetect


client = MongoClient('mongodb:127.0.0.1:27017')
db = client['stage']

collections = db.list_collection_names()

for collection in collections:
    print(collection)
