from fastapi import FastAPI ,Depends, HTTPException,status,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from . import schemas
from .database import get_db,put_in_db


app = FastAPI()

# Mount the static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Create an instance of Jinja2Templates
templates = Jinja2Templates(directory="app/templates")

current_visitor = None
shows_booked = []
exhibits_booked = []



@app.get("/",)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
"""
This is a quick guide how the js should handle the response from the server
1. The response will have a message which will be displayed to the user
2. The response will have options which will be displayed as buttons to the user
3. The response will have next_endpoint which will be the endpoint to hit when the user selects an option
5. The JavaScript should send the option selected by the user to the next_endpoint as a post request in the format 
                {
                     "choice":"Login"
                }
6. The format will change for Login/Signup responses  
                
"""


@app.get('/start',response_model=schemas.MuseBotGeneralResponse)
def start():
    return {
        "message": "Hello! How are you? Iam MuseBot, Please choose from the options below to continue:",
        "options": ["Login", "Signup", "Continue as Guest"],
        "next_endpoint" : {
                                        "Login":"/login",
                                        "Signup":"/signup",    
                                        "Continue as Guest" : "/select_main"
                                    },
    }


@app.post("/signup",response_model=schemas.MuseBotGeneralResponse)
def signup(new_visitor:schemas.UserSignup):
    if new_visitor.model_dump() in get_db()["visitors"]:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"{new_visitor.name} has account kindly login")
    put_in_db('visitors',new_visitor)
    current_visitor = new_visitor
# Currently the visitors are retrived based on index but it should be using id when actual db is implemented
    return {
                    "message": f"Successfullly Signup as {get_db()['visitors'][-1]['name']}",
                    "options": ["Explore Options"],
                    "next_endpoint" : {
                                                    "Explore Options":"/select_main",
                                                },
                }


@app.post('/login')
def login(login_credentials : schemas.UserLogin,db = Depends(get_db)):
    visitors = get_db()["visitors"]
    for visitor in visitors:
        if visitor["email"] == login_credentials.email and visitor["password"] == login_credentials.password:
            current_visitor = visitor
            return {
                            "message": f"Successfullly Logged in  as {visitor["name"]}",
                            "options": ["Explore Options"],
                            "next_endpoint" : {
                                                            "Explore Options":"/select_main",
                                                        },
                        }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrect Login credentials")
        

@app.post("/select_main",response_model = schemas.MuseBotGeneralResponse)
def select_main(response: schemas.UserResponse):
    return {
        "message": "Please choose from the options below:",
        "options": ["Exibits", "Shows","General Museum Tour"],
        "next_endpoint" : {
                                         "Exibits":"/main_response",
                                         "Shows" : "/main_response",
                                         "General Museum Tour" : "/main_response"
                                   },
    }
    
@app.post("/main_response",response_model=schemas.MuseBotGeneralResponse)
def main_response(response: schemas.UserResponse,db =Depends(get_db) ):
    if response.choice == "Exibits":
        return {
            "message": f"Select from the below exhibitions.",
            "options": db["exhibits"],
            "next_endpoint": "/exhibit_response",
        }
    if response.choice == "Shows":
        return {
            "message": f"Select from the below shows.",
            "options": db["shows"],
            "next_endpoint": "/show_response",
        }
    if response.choice == "General Museum Tour": # not yet Implemented
        return {
            "message": "Thankyou.",
            "options": "not Implemented",
            "next_endpoint": "/end",
        }
    raise HTTPException(status_code=404, detail="Invalid choice")
    
@app.post("/exhibit_response",response_model=schemas.MuseBotConfirmationResponse)
def exhibit_response(response: schemas.UserResponse, db=Depends(get_db)):
    # here response choice is the exhibit index for now
    try:
        return {
            "message": "Confirm the exhibition before proceeding.",
            "confirmation_data": db['exhibits'][int(response.choice)-1], # Here response choice is index of the exhibit. but when we implement real db it will be id
            "options" : ["Confirm","Cancel"],
            "next_endpoint" : {
                                         "Confirm":"/exhibit_confirm",
                                         "Cancel" : "/cancel",
                                   },
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@app.post("/show_response",response_model=schemas.MuseBotGeneralResponse)
def exhibit_response(response: schemas.UserResponse, db=Depends(get_db)):
    # here response choice is the show index for now
    try:
        return {
            "message": "Confirm the show before proceeding.",
            "options": [db['shows'][int(response.choice)-1]], # Here response choice is index of the show. but when we implement real db it will be id
            "next_endpoint": "/end",
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))