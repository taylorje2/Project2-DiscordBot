# pip install -U discord.py

import webhoroscopeapi
import discord 
from discord.ext import commands
import logging
import os

# I don't remember how to do this exactly, but I'll look in my notes... Desjardins just showed us how to do this in Advanced Database yesterday...
from dotenv import load_dotenv

# Load the .env file and get the DISCORD_TOKEN variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#--------------------------

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
#^ create a log file, so that if an error occurs we can see which method is going wrong
intents = discord.Intents.default()
intents.message_content = True # allows bot to send message

bot = commands.Bot(command_prefix='/', intents=intents)
#^any commands sent bot start with '/', for instance '/horoscope'

@bot.command
async def horoscope(ctx): #when the user does "/horoscope this method happens"
    horoscope = webhoroscopeapi.get_userhoroscope(ctx.author) #gets the horoscope based on the one asking for it
    await ctx.send(horoscope)

@bot.event
async def setupzodiac(ctx, *, msg):
    zodiac = msg.content.lower
    if zodiac != "aries" or zodiac != "taurus" or zodiac != "gemini" or zodiac != "cancer" or zodiac != "leo" or zodiac != "virgo" or zodiac != "libra" or zodiac != "scorpio" or zodiac != "sagittarius" or zodiac != "capricorn" or zodiac != "aquarius" or zodiac != "pisces":
        await ctx.send("That is not a zodiac sign")
    else:
        await ctx.send("Zodiac Info has been Set Up!")


#--------------------------
# Create a new Discord client and set up event handlers
client = discord.Client()


    

# When the bot is ready, print a message to the console
@client.event
async def on_ready():
    print('Logged in as {client.user}')

# When a message is sent in a channel, check if it starts with "!hello" and respond with "Hello!"
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')