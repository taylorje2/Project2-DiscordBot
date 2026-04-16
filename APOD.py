import requests
from fromapis import nasa_apod
from dotenv import load_dotenv
import os
import discord 
import logging
from discord.ext import commands

load_dotenv()

NASA_API_KEY = os.getenv("APOD_API_KEY")

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

# command for the current day's APOD (/apod)
@bot.command()
async def apod(ctx):
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

        # reply to user with the APOD data in an embed message
        await ctx.send(f"Here's the Astronomy Picture of the Day for {str(apod_data.date)}:")

        # create an embed message with the APOD data
        embed = discord.Embed(title=apod_data.title, description=apod_data.explanation)
        embed.set_image(url=apod_data.url)

        # send the embed message to the channel
        await ctx.send(embed=embed)
    else:
        await ctx.send("Sorry, I couldn't fetch the APOD for today. \nPlease try again later.")

# run the bot
bot.run(TOKEN2, log_handler=handler, log_level=logging.INFO)

# confirmation message in terminal that the bot is running
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


###################################################################################
# DELETE THIS LATER, TESTING PURPOSES ONLY, NOT PART OF FINAL BOT FUNCTIONALITY
###################################################################################
# reply to hello message 
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "hello" in message.content.lower():
        await message.channel.send(f"Hello {message.author.mention}!")

    # respond to all other messages sent
    await bot.process_commands(message)