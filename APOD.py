import requests
from fromapis import nasa_apod
from dotenv import load_dotenv
import os
import discord 
from discord.ext import commands

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")

BASE_URL = "https://api.nasa.gov/planetary/apod"

