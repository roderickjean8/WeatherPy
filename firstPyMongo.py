import pymongo


conn = "mongodb://localhost;27017"
client = pymongo.mongoclient(conn)

db = client.travel

dest = db.destinations.find()


for countries in dest;
print (countries)

db.destinations.insert_one({
    "continent":"africa",
    'country':'madagaskar',
    'major_cities':'roderick Land'
})

count = db.destinations.count()
print ("total doc")