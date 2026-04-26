# Project 2 - Discord Bot
Moon/Horoscope/APOD
Repo for Project 2

# Description

# Features

# Setup Instructions

# Commands
/horoscope
/mooon
/newuser
/getuserinfo
/updateusername
/updateuserzodiac
/delete
/apod
/oldapod

# Code Overview
projectTwo.db

main.py

APOD.py

confirm.py

fromapis.py


# Notes

# Developers
Rachel Smith
Jayden Taylor
Terysa Brewer


# main.py
4/13/26 Made env file complete with token
4/22/26 Added a confirmation message for backend to know whether they've successfully connected to the bot
        Added terminal debugging - the log can get a little overwhelming, but the log detects errors better
        Added greetings - so that we know the bot is acknowledging user messages
        /setupuser 
            changed to /newuser and changed ctx interaction command so that we can use slash commands 
        /horoscope 
            changed ctx to interaction command so that we can use slash commands
4/23/26 Fixed /getuserinfo
4/25/25 /horoscope 
            added if statement for validity checking for existing user
        /getuserinfo
            added in server response, to tell user to check their private messages
        /updateuser
            changed ctx to interaction command so that we can use slash commands
            *issues*
                add a confirm update/change prompt
                add comments
        /updatezodiac
            changed ctx to interaction command so that we can use slash commands
            *issues*
                add a confirm update/change prompt
                add comments
        /delete
            changed ctx to interaction command so that we can use slash commands
            added in server confirmation of deletion
        /moon
            added to main.py
4/26/26 comments added to all methods
        /delete
            added yes/no buttons for user to confirm their delete request
*ideas* 
- once user submits information, have bot create a private channel for interactions
- add ephemeral=True flags to make certain commands visible to only the user
*need to do*
- clean up README.md
- add a "/help" command, and inform new users about help command

# ProjectTwo.db
Relational database that interacts with the bot to hold and retrieve user information. Upon new user creation, a database entry is created for the user, which includes the users username and user inputed zodiac sign, and auto generated user Id number. Database will also reflect all CRUD operations.

# fromapis.py
4/13/26 made code to get zodiac and the user's username to save to table in db
    *Issues*
    - When getting user_id, it gets by index number, but really want last inputs id + 1
4/25/26 added moon API

# confirm.py
Button that give users the opportunity to confirm their inputs before submitting

# gitignore
4/22/26 Added discord.log, __pycache__, and .idea
