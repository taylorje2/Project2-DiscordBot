
#-----------
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
#------------
from pydantic import BaseModel
#------------
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#------------
from fastapi import FastAPI, Depends

#------------------------------------
Base = declarative_base()

# this is the table for the user information
class User(Base):
    __tablename__ = "UserInfo"
    User_Id = Column(Integer, primary_key=True)
    Username = Column(String)
    User_Zodiac = Column(String)

    def __repr__(self):
        return f"{self.User_Id} | { self.Username} | {self.User_Zodiac}"

# this is the model for the user information
class addUser(BaseModel):
    user_id: int
    username: str
    zodiac: str
    def __repr__(self):
        return f"{self.user_id} | { self.username} | {self.zodiac}"

#------------------------------------

DATABASE_URL = "sqlite:///./projectTwo.db"#connection the the database

#create engine to host db sessions
engine = create_engine(DATABASE_URL)

# validating data model matches the db columns
Base.metadata.create_all(bind=engine)

# create factory to make sessions for db transactions
session_factory = sessionmaker(bind=engine)

#function to give diff request endpoints a db session
def get_session():
    session = session_factory()
    try:
        yield session # try keeping the sessin
    finally:
        session.close()#if cant, then stop

app = FastAPI() #creates the api

# endpoints for the api
@app.post("/")
async def save_userinfo(user: addUser, session = Depends(get_session)):
    print("saving...")
    user = User(
        User_Id = user.user_id,
        Username = user.username,
        User_Zodiac = user.zodiac
    )
    session.add(user)
    session.commit()

# method for getting user information
@app.get("/{id}")
def read_userinfo(id: int, session = Depends(get_session)): # Read User
    print("getting...")
    user = session.query(User).filter(User.User_Id == id).first()
    return(user)

# method for changing/updating user information
@app.put("/{id}/{edit}")
def update_username(id: int, edit : str, session = Depends(get_session)): # Update User : Username
    print("updating username...")
    user = session.query(User).filter(User.User_Id == id).first()
    session.delete(user)
    updated_userinfo = User(User_Id = user.User_Id, Username = edit, User_Zodiac = user.User_Zodiac)
    session.add(updated_userinfo)

    session.commit()

    return(user)

# method for changing/updating user zodiac sign
@app.patch("/{id}/{edit}")
def update_zodiac(id: int, edit : str, session = Depends(get_session)): #update user: zodiac
    
    print("updating zodiac...")
    user = session.query(User).filter(User.User_Id == id).first()
    session.delete(user)
    updated_userinfo = User(User_Id = user.User_Id, Username = user.Username, User_Zodiac = edit)
    session.add(updated_userinfo)

    session.commit()
    return(user)

# method for deleting user inforemation
@app.delete("/{id}")
def delete_user(id : int, session = Depends(get_session)):
    user = session.query(User).filter(User.User_Id == id).first()
    session.delete(user)
    session.commit()
    return(user)