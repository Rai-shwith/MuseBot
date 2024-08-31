import json
from typing import Union
from pydantic import BaseModel

def get_db():
    with open('dummy_db/db.json','r') as d:
        db = json.load(d)
    return db

def put_in_db(table_name:str,entity:Union[dict,BaseModel]):
    # Convert the entity to a dictionary if it's a Pydantic model
    if isinstance(entity, BaseModel):
        entity = entity.model_dump()
    db = get_db()
    required_table = db[table_name]
    required_table.append(entity)
    with open('dummy_db/db.json',"w") as d:
        json.dump(db,d,indent=4)
