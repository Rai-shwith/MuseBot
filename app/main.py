from fastapi import FastAPI, Depends
from database import get_db,Base,engine
import schemas,models

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World "}

# Example route to check database connection
@app.get("/users")
def read_users(db=Depends(get_db)):
    # Here you would run a query
    all_users = db.query(models.User).all()
    return all_users

@app.post('/users')
def create_user(user:schemas.UserCreate,db=Depends(get_db)):
    try:
        new_user = models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
    except Exception as e:
        return {"error": e}
    db.refresh(new_user)
    return new_user
