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
		"extra": {
			"city": "Krakow",
			"street": "Kawiory"
		}
	},
	{
		"name": "Edward",
		"description": "Example description",
		"age": 25,
		"extra": {
			"city": "Poznan",
			"street": "Jana Pawla"
		}
	},
	{
		"name": "Jan",
		"description": "Example description",
		"age": 26,
		"extra": {
			"city": "Warszawa",
			"street": "Kawiory"
		}
	},
	{
		"name": "Zenobiusz",
		"description": "Example description",
		"age": 20,
		"extra": {
			"city": "Krakow",
			"street": "Pilsudskiego"
		}
	},
	{
		"name": "Bonifacy",
		"description": "Example description",
		"age": 30,
		"extra": {
			"city": "Krakow",
			"street": "Pilsudskiego"
		}
	}
])

print
print "Inserted data:"
for c in collection.find({}, {"_id": 0}):
	print json.dumps(c, sort_keys=True, indent=4)
	print

print
print "Results with city == Krakow (sorted by age):"
for doc in collection.find({"extra.city": "Krakow"}, {"_id": 0}).sort("age"):
	print json.dumps(doc, sort_keys=True, indent=4)
	print