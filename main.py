# pip install -U discord.py
import discord 
import os

# I don't remember how to do this exactly, but I'll look in my notes... Desjardins just showed us how to do this in Advanced Database yesterday...
from dotenv import load_dotenv

# Load the .env file and get the DISCORD_TOKEN variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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