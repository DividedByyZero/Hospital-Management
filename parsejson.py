import json

def get_data(name):
    f = open(name)
    data = json.load(f)
    return data
    f.close()
