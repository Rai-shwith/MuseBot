from sqlalchemy import Column, Integer, String
from database import Base

# Define your SQLAlchemy model (table)
class User(Base):
    __tablename__ = "users"  # Name of the table

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(Integer,nullable=False,unique=True)
    gender = Column(String)
