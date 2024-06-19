import pymongo,date,json
from datetime import datetime

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hospital"]
collection = db["prescription"]



# Parse date strings to datetime objects
start_date = date.retrive(input("From Date :"))
end_date = date.retrive(input("To Date :"))
print(start_date)
print(end_date)
# Query documents within the specified date range

query = {
    "patient_id": 50006,
}
projection = {"prescriptions": 1, "_id": 0}
results = collection.find(query,projection)
# Iterate over the result
for result in results:
    prescriptions = result["prescriptions"]
    for prescription in prescriptions:
        prescription_date = datetime.strptime(prescription['date'], "%d/%m/%Y")
        prescription_date = prescription_date.date().strftime("%d/%m/%Y")
        if start_date<= prescription_date and end_date>=prescription_date:
           print(json.dumps(prescription,indent=2))
