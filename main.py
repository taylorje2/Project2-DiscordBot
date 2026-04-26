import requests
import fromapis
import discord 
from discord.ext import commands
from discord import app_commands
from confirm import Confirm
import logging
import os
from dotenv import load_dotenv

# Load the .env file and get the DISCORD_TOKEN variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# APOD API key variable and BASE_URL
NASA_API_KEY = os.getenv("APOD_API_KEY")

BASE_URL = "https://api.nasa.gov/planetary/apod"

#--------------------------
# writes ALL activity into discord.log file (for debug)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w') 

intents = discord.Intents.default()
intents.message_content = True # allows bot to send message


bot = commands.Bot(command_prefix='/', intents=intents)
<<<<<<< HEAD

=======
>>>>>>> parent of 5569d1a (Added the bot tree for commands list)
#^any commands sent bot start with '/', for instance '/horoscope'
tree = bot.tree


#--------------------------
# DEBUGGING METHODS
#--------------------------

# syncs tree commands
async def setup_hook():
    await bot.tree.sync()
bot.setup_hook = setup_hook

# when the bot is ready, it will print this message in the terminal
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!') 

# when the bot receives a message, it will print the message content in the terminal, and if the message is a greeting, it will respond with a greeting (for debug purposes)
@bot.event 
async def on_message(message):
    # if the message is from the bot, ignore it
    if message.author.bot: 
    # if message.author == bot.user: 
        return
    print ("USER MESSAGE:", message.content) 
    # if the message is a greeting, respond with a greeting
    if message.content.lower().strip() in ("hello", "hi", "hey"): 
        await message.channel.send("Hello!")
    await bot.process_commands(message) 

# this is for catching any errors that occur with the bot
@bot.tree.error
async def on_app_command_error(interaction, error):
    print (f"[ERROR] An error occurred: {error}")

#-------------------------- END OF DEBUGGING --------------------------


#--------------------------
# BOT COMMANDS
#--------------------------

#------------------------- GET users daily horoscope --------------------------
# method for "/horoscope" command, which retrieves and sends users daily horoscope
@bot.tree.command(name="horoscope", description="Get your daily horoscope")
async def horoscope(interaction: discord.Interaction):
    # Response showing that bot has acknoledged the command
    await interaction.response.send_message("Getting your horoscope...")

    # this method gets the horoscope based on the username of the person asking for it, so it will look up their saved zodiac sign and then get the horoscope for that sign
    horoscopeValidity = requests.get(f"http://localhost:8000/horoscope/{interaction.user.id}")

    # validation check for existing user in the database
    if horoscopeValidity.status_code == 200:
        horoscope = horoscopeValidity.json()
        # Passed validation, sends a followup message with users horoscope
        await interaction.followup.send(f"Here is your horoscope: {horoscope}")
    else:
        # FAILED validation, sends a message informing user that their info is not saved
        await interaction.followup.send("User does not exist, unable to retrieve horoscope")

#---------------- get moon phase -------------
@bot.tree.command(name="moon", description="Get Today's Moon Phase")
async def moon(interaction: discord.Interaction):
    await interaction.response.send_message("Getting moon phase...")

    moon_phase = fromapis.get_moonphase()

    if moon_phase == "Full Moon":
        title = "Full Moon"
        desc = "Today's Moon Phase is a Full Moon!"
        image_url = "https://d.newsweek.com/en/full/2161840/mars-passes-behind-moon.jpg?w=400&e=26926b6b37936c72a323f780c2130e27"
    elif moon_phase == "First Quarter":
        title = "First Quarter"
        desc = "Today's Moon Phase is a First Quarter!"
        image_url = "https://media.istockphoto.com/id/1292676775/photo/first-quarter-moon-also-called-a-half-moon-since-we-see-exactly-50-of-the-moons-visible.jpg?s=170667a&w=0&k=20&c=Kdl0KD0DOOLWlMNec1qn0sfKHnDYRAIAqde859zhMOo="
    else:
        title = "Lase Quarter"
        desc = "Today's Moon Phase is a Lase Quarter!"
        image_url = "https://science.nasa.gov/wp-content/uploads/2023/08/third-quarter.jpg"
    embed = discord.Embed(title=title, description= desc)
    embed.set_image(url=image_url)

    # Passed validation, sends a followup message with users horoscope
    await interaction.followup.send(embed=embed)

    await interaction.followup.send("An error has occurred trying to retrieve the moon phase, please try again later.")


#------------------------- CREATE new user --------------------------
# method for "/newuser" command, which will save the user's information (id, username, and zodiac sign) into the database
@bot.tree.command(name="newuser", description="Set up your user info with your zodiac sign")
async def newUser(interaction: discord.Interaction, zodiac: str):
    userinfo = requests.get(f"http://localhost:8000/{interaction.user.id}").json()
    if userinfo != None:
            await interaction.response.send_message("You have already saved your data")
    else:
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
            # new user data is addeed to the database
            requests.post("http://localhost:8000/", json=user)
        
#-------------------------- GET user information --------------------------
# method for "/getuserinfo" command, which will get the user's information (id, username, and zodiac sign) from the database and send it to the user in a direct message
@bot.tree.command(name="getuserinfo", description="view user information - username and zodiac sign")
async def getuserinfo(interaction: discord.Interaction):
    # get the user information based on the username of the person asking for it, so it will look up their saved information and then send it to them in a direct message
    try:
        userinfo = requests.get(f"http://localhost:8000/{interaction.user.id}").json()
        # send direct message instead to server, incase the id is sensitive info
        await interaction.user.send(f"Your Id is {userinfo['User_Id']}, your username is {userinfo['Username']}, and your saved zodiac is {userinfo['User_Zodiac']}")
        # send message in the server to notify user that information has been sent to DMs
        await interaction.response.send_message("User information has been sent to your direct messages")
    # response to user if they do not exist in the database.
    except:
        await interaction.response.send_message(f"User does not exist, please create new user")

#-------------------------- UPDATE username --------------------------
# method for "/updateusername" command, which updates username, reflecting their changed discord username
@bot.tree.command(name="updateusername", description="update username")
async def changeusername(interaction: discord.Interaction):
    # username in db should reflect that of their discord, retreive user information to validate whether or not user exists in database
    discordusername = interaction.user.name
    userinfo = requests.put(f"http://localhost:8000/{interaction.user.id}/{discordusername}")
    # update response message after successful update status code
    if userinfo.status_code == 200:
        # send direct message instead to server, incase the id is sensitive info
        await interaction.user.send(f"You've changed your discord name, it is now {discordusername}, updated in your horoscope profile.")
        # send message in the server to notify user that information has been sent to DMs
        await interaction.response.send_message(f"{discordusername} has been updated")
    # response to user if they do not exist in the database.
    else:
        await interaction.response.send_message("User does not exist, please create a new user")

#-------------------------- UPDATE user zodiac --------------------------
# method for "/updateuserzodiac" command, which allows users to update their zodiac sign
@bot.tree.command(name="updateuserzodiac", description="update zodiac sign")
async def changezodiac(interaction: discord.Interaction, zodiac: str):
    # get user info
    userinfo = requests.get(f"http://localhost:8000/{interaction.user.id}").json()
    # response to user if they do not exist in the database.
    if not userinfo:
        await interaction.response.send_message("User does not exist, pease create a new user")
        return
    # if user exists, then user will be prompted to enter their zodiac sign
    else:
        zodiac = zodiac.lower() 
        valid = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
        # validation to make sure that user is entering a valid zodiac sign
        if zodiac not in valid:
            await interaction.response.send_message(f"{zodiac} is not a zodiac")
        # update the users zodiac sign
        userinfovalid = requests.patch(f"http://localhost:8000/{interaction.user.id}/{zodiac}")
        # update response message after successful update status code
        if userinfovalid.status_code == 200:
                updateduserinfo = userinfovalid.json()
                # send direct message instead to server, incase the id is sensitive info
                await interaction.user.send(f"Your Id is {userinfo['User_Id']}, your username is {userinfo['Username']} , and your saved zodiac is {zodiac}")
                # send message in the server to notify user that information has been sent to DMs
                await interaction.response.send_message(f"{userinfo['Username']} has changed their zodiac to {zodiac}!")
        # response to user if they do not exist in the database.
        else:
                await interaction.response.send_message("User does not exist, please create a new user")

#-------------------------- DELETE user --------------------------
@bot.tree.command(name="delete", description="Delete user")
async def deleteuser(interaction: discord.Interaction):
    try:
        # check to see if user exists first, retrieve user information
        userinfo = requests.get(f"http://localhost:8000/{interaction.user.id}").json()
        # response message to user if information does not exist
        if not userinfo:
            await interaction.response.send_message("User does not exist, pease create a new user", ephemeral=True)
            return
        # ask user for confirmation before deleting
        confirmdelete = Confirm()
        # response message to user 
        await interaction.response.send_message("\u2757 Are you sure you want to delete your profile?", view=confirmdelete, ephemeral=True)
        await confirmdelete.wait()
        # cancel delete
        if not confirmdelete.value:
            await interaction.followup.send(f"\u274C {userinfo['Username']} cancelled delete", ephemeral=True)  
            return
        # delete user after confirmation
        userdelete = requests.delete(f"http://localhost:8000/{interaction.user.id}")
        if userdelete.status_code == 200:
            await interaction.followup.send(f"\u2705 {userinfo['Username']} deleted", ephemeral=True)
        # response to user if they do not exist in the database.
        else:
            await interaction.followup.send("unable to delete user, try again later", ephemeral=True)
    # catches any possible errors
    except:
        await interaction.response.send_message(f"An error occurred, please try again later", ephemeral=True)

# run the bot with the token, and log handler for debugging
bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)
