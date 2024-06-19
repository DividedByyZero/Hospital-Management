import pymongo
myclient = pymongo.MongoClient('localhost',27017)
mydb = myclient["hospital"]
mycol = mydb["prescription"]

myquery = { "patient_id": 10011 }

mydoc = mycol.find(myquery)
print(mydoc[0])
