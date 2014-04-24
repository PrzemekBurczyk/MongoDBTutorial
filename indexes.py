from pymongo import MongoClient
import pymongo
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
	},
	{
		"name": "Przemek",
		"description": "Example description",
		"age": 21,
		"groups": ["moderator", "admin"]
	},
	{
		"name": "Edward",
		"description": "Example description",
		"age": 56,
	},
	{
		"name": "Przemek",
		"description": "Example description 2",
		"age": 34,
	},
	{
		"name": "Przemek",
		"description": "Example description",
		"age": 90,
		"groups": ["moderator", "admin"]
	},
	{
		"name": "Edward",
		"description": "Example description",
		"age": 11,
	},
	{
		"name": "Przemek",
		"description": "Example description 2",
		"age": 24,
	}
])

print
print "Inserted data:"
for c in collection.find({}, {"_id": 0}):
	print json.dumps(c, sort_keys=True, indent=4)
	print

print
print "Results without indexes:"
print json.dumps(collection.find({"age": {"$gt": 30}}).sort("age").explain(), sort_keys=True, indent=4)

index = collection.create_index("age")	

print
print "Results with indexes on age:"
print json.dumps(collection.find({"age": {"$gt": 30}}).sort("age").explain(), sort_keys=True, indent=4)

collection.drop_index(index)