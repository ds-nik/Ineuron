import pymongo

client = pymongo.MongoClient("mongodb+srv://ds_nik:nikhil1234@cluster0.tyi3g6e.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"nikhil",
    "email": "nkothari135@gmail.com",
    "surname": "kothari"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)