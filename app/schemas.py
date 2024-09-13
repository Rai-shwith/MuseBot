from pydantic import BaseModel
from typing import Union

class UserCreate(BaseModel):
    name : str
    email : str
    phone_number : str
    gender:str
    
    class Config:
        from_attribute = True
    