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

# token specifically for apod bot
TOKEN2 = os.getenv("APOD_BOT_TOKEN")

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

# command list tree (shows a list of bot commands when "/" is entered)
tree = bot.tree

# command for the current day's APOD (/apod)
@bot.tree.command(name="apod", description="Get the NASA APOD for today")
async def apod(interaction: discord.Interaction):
    # interaction defer to prevent bot timeout
    await interaction.response.defer()

    # parameters for the API request
    params = {
        "api_key": NASA_API_KEY
    }

    # make the API request and get the response
    apod_response = requests.get(BASE_URL, params=params)

    # check if the request was successful
    if apod_response.status_code == 200:
        # parse the response JSON into a nasa_apod object
        apod_data = nasa_apod(**apod_response.json())

        # create an embed message with the APOD data. Embed will have a purple sidebar
        embed = discord.Embed(title=f"{apod_data.title}\nDate: {str(apod_data.date)}\n", description=apod_data.explanation, color=0x800080)
        embed.set_image(url=apod_data.url)

        # send the embed message to the channel and mention the requesting user
        await interaction.followup.send(content=interaction.user.mention, embed=embed)
    else:
        await interaction.followup.send("Sorry, I couldn't fetch the APOD for today. \nPlease try again later.")