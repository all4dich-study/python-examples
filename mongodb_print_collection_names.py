from pymongo import MongoClient
conn = MongoClient()
db = conn.get_database('cerberusLog')
coll = db.get_collection('starfish-drd4tv-verify-mtka5lr')
coll.find().count()
