# Project 2 - Discord Bot
Moon/Horoscope/APOD
Repo for Project 2

# Description
Astro bot was designed for those who enjoy and have an interest in astronomy and astrological signs. The bot was designed with the intentions of giving users a daily dose of personalized content on their interests.

# Features
- Tells users their daily horoscope
- Displays the daily moon phase
- Display daily APOD
- Users are able to request previous APODS

# Setup Instructions
1. Clone this repository
    git clone https://github.com/taylorje2/Project2-DiscordBot.git
2. Install dependencies
    pip install -r requirements.txt
3. Add your bot token and APOD API key (in .env file):
    DISCORD_TOKEN=insert_your_bot_token_here
    APOD_API_KEY=insert_your_apod_api_key_here
4. Run Uvicorn
    python -m uvicorn fromapis:app --host localhost --port 8000
5. Run the bot
    python main.py

# Commands
/help - shows available commands

/horoscope - shows daily horoscope

/moon - shows daily moon phase

/newuser - creation of new users

/getuserinfo - shows user information

/updateusername - updates username, if they've recently changed their discord username

/updateuserzodiac - updates user zodiac sign

/delete - deletes user information

/apod - shows the apod od the day

/oldapod - shows older APOD from a specified date (use YYYY-MM-DD format)

# Code Overview
ProjectTwo.db
Relational database that interacts with the bot to hold and retrieve user information.

main.py
Holds all of the technical code that makes the bot run, as well as debugging methods and all of the discord "/" command methods

confirm.py
Class that creates buttons that give users the opportunity to confirm their inputs before submitting

fromapis.py
Holds all of the code that allows the bot to interact with databases.

APOD.txt
Was originally as APOD.py for testing purpose, and changed into a txt. when the branch was merged with the main branch
*APOD.py can be ignored. It was only used for testing purposes for the APOD API and its commands.*

# Notes

# Developers
Rachel Smith

Jayden Taylor

Terysa Brewer

