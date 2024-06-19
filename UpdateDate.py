from pymongo import MongoClient
from datetime import datetime
import date
# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['hospital']  # Replace 'your_database' with your actual database name
collection = db['prescription']   # Replace 'patients' with your collection name

# Define the query to match all documents that have a prescriptions array
query = { "prescriptions": { "$exists": True } }

# Retrieve all documents that match the query
documents = collection.find(query)
c=0
# Iterate over each document
for doc in documents:
    c+=1
    updated_prescriptions = []
    print(f"Updated document with _id: {doc['patient_id']}")
    for prescription in doc.get('prescriptions', []):
        # Convert the date string to datetime object
        date_str = prescription.get('date', '')
        if date_str[-1] != 'Z':
            print(doc['patient_id'])
            date_obj = datetime.strptime(date_str, "%d/%m/%Y")
            # Format datetime object to ISO format
            iso_date = date_obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            prescription['date'] = iso_date
        updated_prescriptions.append(prescription)
    
    # Update the document with the modified prescriptions array
    updated_document = {
        "$set": {
            "prescriptions": updated_prescriptions
        }
    }
    
    # Perform the update for the current document
    result = collection.update_one({ "_id": doc["_id"] }, updated_document)
    

print("All documents updated successfully.")
