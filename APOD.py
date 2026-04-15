import requests
from fromapis import nasa_apod
from dotenv import load_dotenv
import os
import discord 
import logging
from discord.ext import commands

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")

BASE_URL = "https://api.nasa.gov/planetary/apod"

TOKEN = os.getenv("DISCORD_TOKEN")

# writes all activity into discord.log file (for debug)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# permissions for the bot
intents = discord.Intents.default()

# allows bot to send messages
intents.message_content = True 

# allows bot access to server member data
intents.members = True

# set command prefix
bot = commands.Bot(command_prefix='/', intents=intents)
