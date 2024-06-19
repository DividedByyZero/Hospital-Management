def patients(data):
    allData =[]
    for x in data:
        allData.append((x['patient_id'],x['name'],x['age'],x['sex']))
    return allData
def physicians(data):
    allData =[]
    for x in data:
        allData.append((x["prescriptions"][-1]["physician"]["id"],x["prescriptions"][-1]["physician"]["name"],x["prescriptions"][-1]["physician"]["specialist"]))
    return allData