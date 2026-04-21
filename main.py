# pip install -U discord.py
import requests
import fromapis
import discord 
from discord.ext import commands
import logging
import os
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
        user = {
            "user_id" : ctx.author.id,
            "username" :ctx.author.name,
            "zodiac" : zodiac
        }
        
        requests.post("http://localhost:8000/", json=user)

@bot.command()
async def getuserinfo(ctx):
    try:
        userinfo = requests.get(f"http://localhost:8000/{ctx.author.id}").json()
        await ctx.author.send(f"Your Id is {userinfo["User_Id"]}, your username is {userinfo["Username"]} , and your saved zodiac is {userinfo["User_Zodiac"]}")
        # ^ send direct message instead to server, incase the id is sensitive info
    except:
        await ctx.send(f"You haven't set up your user info, therefore cannot get that info :)")

@bot.command()
async def changeusername(ctx, *, username):
    try:
        userinfo = requests.put(f"http://localhost:8000/{ctx.author.id}/{username}").json()
        await ctx.author.send(f"Your Id is {userinfo["User_Id"]}, your username is {username} , and your saved zodiac is {userinfo["User_Zodiac"]}")
        await ctx.send(f"{userinfo["Username"]} has changed their username to {username}!")

    except:
        await ctx.send(f"You haven't set up your user info, therefore cannot update that info :)")

@bot.command()
async def changezodiac(ctx, *, zodiac):
    try:
        zodiac = zodiac.lower() 

        if zodiac != "aries" and zodiac != "taurus" and zodiac != "gemini" and zodiac != "cancer" and zodiac != "leo" and zodiac != "virgo" and zodiac != "libra" and zodiac != "scorpio" and zodiac != "sagittarius" and zodiac != "capricorn" and zodiac != "aquarius" and zodiac != "pisces":
            await ctx.send(f"{zodiac} is not a zodiac")
        else:
            userinfo = requests.patch(f"http://localhost:8000/{ctx.author.id}/{zodiac}").json()
            await ctx.author.send(f"Your Id is {userinfo["User_Id"]}, your username is {userinfo["Username"]} , and your saved zodiac is {zodiac}")
            await ctx.send(f"{userinfo["Username"]} has changed their zodiac to {zodiac}!")

    except:
        await ctx.send(f"You haven't set up your user info, therefore cannot update that info :)")

@bot.command()
async def deleteuser(ctx):
    try:
        user = requests.delete(f"http://localhost:8000/{ctx.author.id}").json()
        await ctx.send(f"{user["Username"]} has had their data deleted.")
    except:
        await ctx.send(f"That user hasn't set up their data, therefore nothing to delete")


bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)