import pymongo

client = pymongo.MongoClient()
db = client.artists
co = db.my_collection

for record in co.find({"tags.value": "dance"}).sort([("rating.value", pymongo.DESCENDING)]).limit(10):
	print(record)