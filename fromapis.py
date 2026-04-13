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

class Horoscope(Base):
    __tablename__ = "DailyHoroscope"
    Id = Column(Integer, primary_key=True)
    horoscopeDate = Column(String)
    horoscopeSign = Column(String)
    horoscopeText = Column(String)

    def __repr__(self):
        return f"{self.Id} | {self.horoscopeDate} | {self.horoscopeSign} | {self.horoscopeText}"


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

zodiac_signs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
#all the signs used in \/

zodiac_count = 0

def get_allhoroscope(zodiac_count):

    for zodiac in zodiac_signs:
        zodiac_horoscope = f"https://freehoroscopeapi.com/api/v1/get-horoscope/daily?sign={zodiac}"
        
        h_info = requests.get(zodiac_horoscope).json()

        api_response = APIResponse(**h_info)

        horoscope = { #divides the 
                "Date" : api_response.data.date,
                "Sign" : api_response.data.sign,
                "Horoscope" : api_response.data.horoscope
                } 
        print(horoscope)

        zodiac_count += 1

        to_add = Horoscope(Id = zodiac_count, horoscopeDate = horoscope["Date"], horoscopeSign = horoscope["Sign"], horoscopeText = horoscope["Horoscope"] )

        session.add(to_add)

    session.commit()

def save_userinfo(zodiac: str, author : str):

    try:
        numOfUsers = User.__tablename__.index
    finally:
        numOfUsers = 0

    to_add = User(User_Id = numOfUsers + 1, Username = author, User_Zodiac = zodiac)
    session.add(to_add)

    session.commit()

#-------------------------------






