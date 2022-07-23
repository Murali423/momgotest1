import pymongo

client = pymongo.MongoClient("mongodb+srv://murali:mongodb123@cluster0.fxgp1cv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

db1 = client['mongotest']
coll = db1['test']

# record = coll.find()
# for i in record:
#     print(i)

#data = coll.find({'companyName': 'iNeuron'})
data =coll.find({'courseOffered':{"$gt":"E"}})
for i in data:
    print('/------------------/')
    print(i)