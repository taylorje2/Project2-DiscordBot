# pip install -U discord.py

import fromapis
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

@bot.command()
async def horoscope(ctx): #when the user does "/horoscope this method happens"
    horoscope = fromapis.get_userhoroscope(ctx.author.name) #gets the horoscope based on the one asking for it
    await ctx.send(horoscope)

@bot.command()
async def setupzodiac(ctx, *, zodiac):
    zodiac = zodiac.lower()
    if zodiac != "aries" and zodiac != "aries" and zodiac != "taurus" and zodiac != "gemini" and zodiac != "cancer" and zodiac != "leo" and zodiac != "virgo" and zodiac != "libra" and zodiac != "scorpio" and zodiac != "sagittarius" and zodiac != "capricorn" and zodiac != "aquarius" and zodiac != "pisces":
        await ctx.send(f"{zodiac} is not a zodiac")
    else:
        await ctx.send(f"Your saved zodiac is {zodiac}")
        fromapis.save_userinfo(zodiac, ctx.author.name)



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