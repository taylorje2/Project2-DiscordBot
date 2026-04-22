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
# writes ALL activity into discord.log file (for debug)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w') 

# # creates a log handler for ONLY errors, which will write all errors into error.log file (for debug)
# errorHandler = logging.FileHandler(filename='error.log', encoding='utf-8', mode='w')
# errorHandler.setLevel(logging.ERROR)

intents = discord.Intents.default()
intents.message_content = True # allows bot to send message


bot = commands.Bot(command_prefix='/', intents=intents)
#^any commands sent bot start with '/', for instance '/horoscope'


#--------------------------
# DEBUGGING METHODS
#--------------------------
# when the bot is ready, it will print this message in the terminal
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!') 

# when the bot receives a message, it will print the message content in the terminal, and if the message is a greeting, it will respond with a greeting (for debug purposes)
@bot.event 
async def on_message(message):
    # if the message is from the bot, ignore it
    if message.author == bot.user: 
        return
    print ("USER MESSAGE:", message.content) 
    # if the message is a greeting, respond with a greeting
    if message.content.lower().strip() in ("hello", "hi", "hey"): 
        await message.channel.send("Hello!")
    await bot.process_commands(message) 

# when an error occurs with a command, it will print the error in the terminal
@bot.event
async def on_app_command_error(ctx, error):
    logging.exception("An error occurred")
    print (f"[ERROR] An error occurred: {error}")

# this is for catching any errors that occur with the bot
@bot.tree.error
async def on_app_command_error(interaction, error):
    print (f"[ERROR] An error occurred: {error}")

#-------------------------- END OF DEBUGGING --------------------------


#--------------------------
# BOT COMMANDS
#--------------------------
# this is the method for the "/horoscope" command, which will get the user's horoscope based on their saved zodiac sign
@bot.tree.command(name="horoscope", description="Get your daily horoscope")
async def horoscope(interaction: discord.Interaction):
    # we can remove this... I just wanted to show that the bot was acknowledging the command for testing purposes
    await interaction.response.send_message("Getting your horoscope...")
    # this method gets the horoscope based on the username of the person asking for it, so it will look up their saved zodiac sign and then get the horoscope for that sign
    horoscope = fromapis.get_userhoroscope(interaction.user.name)
    await interaction.edit_original_response(content=horoscope)

# @bot.command()
# async def horoscope(ctx): #when the user does "/horoscope this method happens"
#     horoscope = fromapis.get_userhoroscope(ctx.author.name) #gets the horoscope based on the one asking for it
#     await ctx.send(horoscope)

#------------------------- CREATE new user --------------------------
# this method is for the "/newuser" command, which will save the user's information (id, username, and zodiac sign) into the database
@bot.tree.command(name="newuser", description="Set up your user info with your zodiac sign")
async def newUser(interaction: discord.Interaction, zodiac: str):
    zodiac = zodiac.lower()
    # validation to make sure that user is entering a valid zodiac sign
    valid = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
    if zodiac not in valid:
        # if the zodiac sign is not valid, a message will be sent to the user saying that it is not a valid zodiac sign
        await interaction.response.send_message(f"{zodiac} is not a zodiac")
    else:
        # if the zodiac sign is valid, a message will be sent to the user confirming that their zodiac sign has been saved, and then their information will be sent to the database to be saved
        await interaction.response.send_message(f"Your saved zodiac is {zodiac}")
        # create a user object with the user's information, which will be sent to the database
        user = {
            "user_id" : interaction.user.id,
            "username" : interaction.user.name,
            "zodiac" : zodiac
        }

# @bot.command()
# async def setupuser(ctx, *, zodiac):
#     zodiac = zodiac.lower()
#     if zodiac != "aries" and zodiac != "taurus" and zodiac != "gemini" and zodiac != "cancer" and zodiac != "leo" and zodiac != "virgo" and zodiac != "libra" and zodiac != "scorpio" and zodiac != "sagittarius" and zodiac != "capricorn" and zodiac != "aquarius" and zodiac != "pisces":
#         await ctx.send(f"{zodiac} is not a zodiac")
#     else:
#         await ctx.send(f"Your saved zodiac is {zodiac}")
#         user = {
#             "user_id" : ctx.author.id,
#             "username" :ctx.author.name,
#             "zodiac" : zodiac
#         }
        
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





