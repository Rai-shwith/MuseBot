import os 
import json

def get_db():
    with open('dummy_db/db.json', 'r') as f:
        data = json.load(f)
    return data
