import pymongo

client = pymongo.MongoClient("mongodb+srv://murali:mongodb123@cluster0.fxgp1cv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

db1 = client['inventory']
coll = db1['test3']
data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
#coll.insert_many(data)
r = coll.find()
#r = coll.find({"status":"A"})
# r = coll.find({'status':{'$in':['A','P']}})
#r = coll.find({'status':{'$gt' : 'C'}})
#r = coll.find({'qty':{'$gte' : 75}})
#r = coll.find({'item':'sketch pad','qty':95})
#r = coll.find({'item':'sketch pad','qty':{'$gt':75}})
#r = coll.find({'$or':[{'item':'sketch pad'},{'qty':{'$gte':100}} ]})
#coll.update_one({'item':'canvas'},{'$set':{'item':'murali'}})
#coll.delete_one({'item':'murali'})
#r = coll.find({'item':'murali'})
for i in r:
    print(i)