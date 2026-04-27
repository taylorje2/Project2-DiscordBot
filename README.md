# Project 2 - Discord Bot
Moon/Horoscope/APOD
Repo for Project 2

# Description
Astro bot was designed for those who enjoy and have an interest in astronomy and astrological signs. The bot was designed with the intention of giving users a daily dose of personalized content on their interests.

# Features
- Tells users their daily horoscope
- Displays the daily moon phase
- Display daily APOD (Astronomy Picture of the Day)
- Displays user-requested past APODs

# Setup Instructions
1. Clone this repository
    git clone https://github.com/taylorje2/Project2-DiscordBot.git
2. Install dependencies
    pip install -r requirements.txt
3. Add your bot token and APOD API key (in .env file):
    DISCORD_TOKEN=insert_your_bot_token_here
    APOD_API_KEY=insert_your_apod_api_key_here
    *On your Discord bot settings, turn on all intents:*
        *Presence Intent*
        *Server Members Intent*
        *Message Content Intent*
4. Run Uvicorn
    python -m uvicorn fromapis:app --host localhost --port 8000
5. Run the bot
    python main.py

# Notes
- APOD API key was retrieved from the NASA Open APIs site: https://api.nasa.gov/
- NASA only provides APODs from 06-16-1995 to the current date.

# Commands
/help - shows available commands

/newuser - creation of new users

/getuserinfo - shows user information

/updateusername - updates username, if they've recently changed their Discord username

/updateuserzodiac - updates user zodiac sign

/delete - deletes user information

/horoscope - shows daily horoscope

/moon - shows daily moon phase

/apod - shows the apod of the day

/oldapod - shows older APOD from a specified date (use YYYY-MM-DD format)
Database does not go past 1995-06-16

# Code Overview
### ProjectTwo.db
Relational database that interacts with the bot to hold and retrieve user information.

### main.py
Holds all of the technical code that makes the bot run, as well as debugging methods and all of the Discord "/" command methods

### fromapis.py
Holds all of the code that allows the bot to interact with databases.

### confirm.py
Holds the code that creates buttons that give users the opportunity to confirm their inputs before submitting

### help.py
Holds the code for the embedded help command

### APOD.txt
Was originally named APOD.py for testing purposes, and changed into a .txt when the branch was merged with the main branch
*APOD.py can be ignored. It was only used for testing purposes for the APOD API and its commands.*

# Developers
Rachel Smith

Jayden Taylor

Terysa Brewer

# Outside Resources
Github Docs - https://docs.github.com/en

Discord Developer Docs - https://docs.discord.com/developers/

Discordpy - https://discordpy.readthedocs.io/

Pycord Guide - https://guide.pycord.dev/

Real Python - https://realpython.com/how-to-make-a-discord-bot-python/

Stack Overflow
