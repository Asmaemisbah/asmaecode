import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client['stage']

if db.command('ping'):
    print('connected')