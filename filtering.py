from pymongo import MongoClient
import json
import datetime
client = MongoClient("localhost", 27017)
db = client.my_db
collection = db.my_collection

collection.remove()

collection.insert([
	{
		"name": "Przemek",
		"description": "Example description",
		"age": 21,
		"groups": ["moderator", "admin"]
	},
	{
		"name": "Edward",
		"description": "Example description",
		"age": 30,
	},
	{
		"name": "Przemek",
		"description": "Example description 2",
		"age": 25,
	}
])

print
print "Inserted data:"
for c in collection.find({}, {"_id": 0}):
	print json.dumps(c, sort_keys=True, indent=4)
	print

print
print "Results age > 25 or groups exist:"
for doc in collection.find({ "$or": [{ "age": { "$gt": 25 } }, { "groups": { "$exists": True } }] }, {"_id": 0}):
	print json.dumps(doc, sort_keys=True, indent=4)
	print