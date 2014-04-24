from pymongo import MongoClient
import json
client = MongoClient("localhost", 27017)
db = client.my_db
collection = db.my_collection

collection.remove()

collection.insert([
    {"kind": "big", "type": "A", "value": 1},
    {"kind": "big", "type": "B", "value": 2},
    {"kind": "small", "type": "B", "value": 3},
    {"kind": "big", "type": "A", "value": 4},
    {"kind": "small", "type": "A", "value": 5},
    {"kind": "big", "type": "B", "value": 6}
])

print
print "Inserted data:"
for c in collection.find({}, {"_id": 0}):
	print json.dumps(c, sort_keys=True, indent=4)
	print
	
print 
print "Aggregation result:"
print json.dumps(collection.aggregate([
	{"$match": 
		{"kind": "big"}
	}, 
	{"$group": 
		{
			"_id": "$type", 
			"total": {"$sum": "$value"},
			"averageValue": {"$avg": "$value"}
		}
	}
]), sort_keys=True, indent=4)