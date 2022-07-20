import pymongo

client = pymongo.MongoClient("mongodb+srv://murali:mongodb123@cluster0.fxgp1cv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={
   "name": "murali",
    "email":"1murali5teja@gmail.com",
    "surname" :"murali"
}

d2 ={
   "name": "murali",
    "email":"1murali5teja@gmail.com",
    "surname" :"murali"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)