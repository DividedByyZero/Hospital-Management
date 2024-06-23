import pymongo,date,json
from datetime import datetime

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["hospital"]
collection = db["prescription"]



# Parse date strings to datetime objects
start_date = date.retrive(input("From Date :"))
end_date = date.retrive(input("To Date :"))
start_date = datetime.strptime(start_date, '%d/%m/%Y')
end_date = datetime.strptime(end_date, '%d/%m/%Y')
print(start_date)
print(end_date)
# Query documents within the specified date range
id = 50006
query = {
    "patient_id": 50006,
    "prescriptions.date": {
        "$gte": start_date,
        "$lte": end_date
    }
}

# Projection to return only necessary fields (optional)
projection = {
    "prescriptions": {
        "$elemMatch": {
            "date": {
                "$gte": start_date,
                "$lte": end_date
            }
        }
    }
}

results = collection.find(query)
# Iterate over the result
for document in results:
    print(f"Name : {document['name']}")
    sorted_prescription = sorted(
        document['prescriptions'],
        key = lambda x : (datetime.strptime(str(x['date']), "%Y-%m-%d %H:%M:%S")).strftime("%Y-%m-%d"),
        reverse=True
    )
    for pres in sorted_prescription:
        if pres['date'] >= start_date and pres['date'] <= end_date:
            print(f"Date {pres['date']}")
            print(pres)
    break
