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

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w') # writes all activity into discord.log file (for debug)
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
async def setupuser(ctx, *, zodiac):
    zodiac = zodiac.lower()
    if zodiac != "aries" and zodiac != "taurus" and zodiac != "gemini" and zodiac != "cancer" and zodiac != "leo" and zodiac != "virgo" and zodiac != "libra" and zodiac != "scorpio" and zodiac != "sagittarius" and zodiac != "capricorn" and zodiac != "aquarius" and zodiac != "pisces":
        await ctx.send(f"{zodiac} is not a zodiac")
    else:
        await ctx.send(f"Your saved zodiac is {zodiac}")
        fromapis.save_userinfo(zodiac, ctx.author.name, ctx.author.id)

@bot.command()
async def getuserinfo(ctx):
    try:
        userinfo = fromapis.read_userinfo(ctx.author.id)
        await ctx.author.send(f"Your Id is {userinfo[0]}, your username is {userinfo[2]} , and your saved zodiac is {userinfo[1]}")
        # ^ send direct message instead to server, incase the id is sensitive info
    except:
        await ctx.send(f"You haven't set up your user info, therefore cannot get that info :)")

@bot.command()
async def changeusername(ctx, *, username):
    try:
        userinfo = fromapis.update_username(ctx.author.id, username)
        await ctx.author.send(f"Your Id is {userinfo[0]}, your username is {userinfo[2]} , and your saved zodiac is {userinfo[1]}")
        await ctx.send(f"{userinfo[2]} has changed their username!")

    except:
        await ctx.send(f"You haven't set up your user info, therefore cannot update that info :)")

@bot.command()
async def changezodiac(ctx, *, zodiac):
    try:
        zodiac = zodiac.lower() 

        if zodiac != "aries" and zodiac != "taurus" and zodiac != "gemini" and zodiac != "cancer" and zodiac != "leo" and zodiac != "virgo" and zodiac != "libra" and zodiac != "scorpio" and zodiac != "sagittarius" and zodiac != "capricorn" and zodiac != "aquarius" and zodiac != "pisces":
            await ctx.send(f"{zodiac} is not a zodiac")
        else:
            userinfo = fromapis.update_zodiac(ctx.author.id, zodiac)
            await ctx.author.send(f"Your Id is {userinfo[0]}, your username is {userinfo[2]} , and your saved zodiac is {userinfo[1]}")
            await ctx.send(f"{userinfo[2]} has changed their zodiac to {userinfo[1]}!")

    except:
        await ctx.send(f"You haven't set up your user info, therefore cannot update that info :)")


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