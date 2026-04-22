# Project 2 - Discord Bot
Moon/Horoscope/APOD
Repo for Project 2

# main.py
4/13/26 Made env file complete with token
4/22/26 Added a confirmation message for backend to know whether they've successfully connected to the bot
4/22/26 Added terminal debugging, added greetings 

# zodiac.py
4/15/26 removed, no longer needed - info is in the main.py

# Horoscope.sql --> Horoscope.sqlite
4/21/26 removed - we decided to not do this anymore

# fromapis.py
4/13/26 made code to get zodiac and the user's username to save to table in db
    *Issues*
    - When getting user_id, it gets by index number, but really want last inputs id + 1
