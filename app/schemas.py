from pydantic import BaseModel ,EmailStr
from typing import Union

class UserResponse(BaseModel):
    choice: str
    
class MuseBotMessageOnly(BaseModel): 
    # This is a response where only message is sent . The frontend should quickly go to the next endpoint
    message : str
    next_endpoint : Union[dict,str]

class MuseBotGeneralResponse(MuseBotMessageOnly):
    options: list
    
class MuseBotConfirmationResponse(MuseBotGeneralResponse):
    confirmation_data : dict
    
class UserSignup(BaseModel):
    visitor_id: int
    name: str
    email : EmailStr
    password : str
    phone_number : int
    preferred_language : str
    
class UserLogin(BaseModel):
    email : EmailStr
    password : str