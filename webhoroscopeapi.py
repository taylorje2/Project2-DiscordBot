import requests
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer


#------------------------------------

class Horoscope(BaseModel):
    date : str
    sign : str
    horoscope : str
    
    

class APIResponse(BaseModel):
    data : Horoscope

   
    
#------------------------------------

zodiac_signs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]

zodiac_counter = 0

def get_horoscope():

    for zodiac in zodiac_signs:
        zodiac_horoscope = f"https://freehoroscopeapi.com/api/v1/get-horoscope/daily?sign={zodiac}"
        
        h_info = requests.get(zodiac_horoscope).json()

        api_response = APIResponse(**h_info)

        print(api_response)
        horoscope = {
                "Date" : api_response.data.date,
                "Sign" : api_response.data.sign,
                "Horoscope" : api_response.data.horoscope
                } 
        print(horoscope)
        
        to_add = HoroscopeTable(horoscope)

        session.add(to_add)

        session.commit()

get_horoscope()

#-------------------------------

SQLALCHEMY_DATABASE_URL = "sqlite:///./data.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

# This binds our ORM class models
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)

session = Session()

class HoroscopeTable(Base):
    __tablename__ = "DailyHoroscope"
    Id = Column(Integer, primary_key=True)
    horoscopeDate = Column(String),
    horoscopeSign = Column(String),
    horoscopeText = Column(String)

    def __repr__(self):
        return f"{self.Id} | {self.horoscopeDate} | {self.horoscopeSign} | {self.horoscopeText}"
