import requests
#-----------
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
#------------
from pydantic import BaseModel
#------------
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#------------------------------------
Base = declarative_base()

class User(Base):
    __tablename__ = "UserInfo"
    User_Id = Column(Integer, primary_key=True)
    Username = Column(String)
    User_Zodiac = Column(String)

    def __repr__(self):
        return f"{self.Id} | {self.Zodiac}"

#------------------------------------

class APIHoroscope(BaseModel): # the response cut up into the details(what we want)
    date : str
    sign : str
    horoscope : str
    

class APIResponse(BaseModel): #this is what the api responds with
    data : APIHoroscope

#------------------------------------

SQLALCHEMY_DATABASE_URL = "sqlite:///./projectTwo.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# This binds our ORM class models
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)

session = Session()
    
#------------------------------------



def save_userinfo(zodiac: str, author : str):

    try:
        numOfUsers = User.__tablename__.index
    finally:
        numOfUsers = 0

    to_add = User(User_Id = numOfUsers + 1, Username = author, User_Zodiac = zodiac)
    session.add(to_add)

    session.commit()


def get_userhoroscope(author : str):

    user = session.query(User).filter(User.Username == author).first()

    
    zodiac_horoscope = f"https://freehoroscopeapi.com/api/v1/get-horoscope/daily?sign={user.User_Zodiac}"
    
    h_info = requests.get(zodiac_horoscope).json()

    api_response = APIResponse(**h_info)

    horoscope = { #divides the api response
                "Date" : api_response.data.date,
                "Sign" : api_response.data.sign,
                "Horoscope" : api_response.data.horoscope
                } 
    
    return(horoscope["Horoscope"])
            
#-------------------------------






