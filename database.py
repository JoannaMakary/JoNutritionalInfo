import pymongo

client = pymongo.MongoClient("mongodb+srv://dbUser:bV2W3yCmJViuKww@cluster0.3gxki.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test
