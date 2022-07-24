import pymongo

client = pymongo.MongoClient("mongodb+srv://ds_nik:nikhil1234@cluster0.tyi3g6e.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = collection.find({"companyName" : "iNeuron"})
for i in data:
    print(i)