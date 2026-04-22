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


#-------------------------- Debugging Within the Terminal --------------------------
# when the bot is ready, it will print this message in the terminal
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!') 

# when the bot receives a message, it will print the message content in the terminal (for debug purposes)
@bot.event 
async def on_message(message):
    # if the message is from the bot, ignore it
    if message.author == bot.user: 
        return
    print ("RESPONSE:", message.content) 
    # if the message is a greeting, respond with a greeting
    if message.content.lower().strip() in ("hello", "hi", "hey"): 
        await message.channel.send("Hello!")
    await bot.process_commands(message) 
#---------------------------- End of Debugging Within the Terminal --------------------------


#--------------------------
@bot.command()
async def horoscope(ctx): #when the user does "/horoscope this method happens"
    horoscope = fromapis.get_userhoroscope(ctx.author.name) #gets the horoscope based on the one asking for it
    await ctx.send(horoscope)

# CREATE new user
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

# method for getting user information
@bot.command()
async def getuserinfo(ctx):
    try:
        userinfo = requests.get(f"http://localhost:8000/{ctx.author.id}").json()
        await ctx.author.send(f"Your Id is {userinfo['User_Id']}, your username is {userinfo['Username']}, and your saved zodiac is {userinfo['User_Zodiac']}")
        # ^ send direct message instead to server, incase the id is sensitive info
    except:
        await ctx.send(f"You haven't set up your user info, therefore cannot get that info :)")

# methods for changing/updating user information
@bot.command()
async def changeusername(ctx, *, username):
    try:
        userinfo = requests.put(f"http://localhost:8000/{ctx.author.id}/{username}").json()
        await ctx.author.send(f"Your Id is {userinfo['User_Id']}, your username is {username} , and your saved zodiac is {userinfo['User_Zodiac']}")
        await ctx.send(f"{userinfo['Username']} has changed their username to {username}!")

    except:
        await ctx.send(f"You haven't set up your user info, therefore cannot update that info :)")

# method for changing/updating user zodiac sign
@bot.command()
async def changezodiac(ctx, *, zodiac):
    try:
        zodiac = zodiac.lower() 

        if zodiac != "aries" and zodiac != "taurus" and zodiac != "gemini" and zodiac != "cancer" and zodiac != "leo" and zodiac != "virgo" and zodiac != "libra" and zodiac != "scorpio" and zodiac != "sagittarius" and zodiac != "capricorn" and zodiac != "aquarius" and zodiac != "pisces":
            await ctx.send(f"{zodiac} is not a zodiac")
        else:
            userinfo = requests.patch(f"http://localhost:8000/{ctx.author.id}/{zodiac}").json()
            await ctx.author.send(f"Your Id is {userinfo['User_Id']}, your username is {userinfo['Username']} , and your saved zodiac is {zodiac}")
            await ctx.send(f"{userinfo['Username']} has changed their zodiac to {zodiac}!")

    except:
        await ctx.send(f"You haven't set up your user info, therefore cannot update that info :)")

# method for deleting user
@bot.command()
async def deleteuser(ctx):
    try:
        user = requests.delete(f"http://localhost:8000/{ctx.author.id}").json()
        await ctx.send(f"{user['Username']} has had their data deleted.")
    except:
        await ctx.send(f"That user hasn't set up their data, therefore nothing to delete")

# run the bot with the token, and log handler for debugging
bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)





