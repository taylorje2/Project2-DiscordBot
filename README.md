# Project 2 - Discord Bot
Moon/Horoscope/APOD
Repo for Project 2

# main.py
4/13/26 Made env file complete with token
4/22/26 Added a confirmation message for backend to know whether they've successfully connected to the bot
        Added terminal debugging - the log can get a little overwhelming, but the log detects errors better
        Added greetings - so that we know the bot is acknowledging user messages
        Fixed f-strings so that /getuserinfo and /deleteuser responds to the user
        Fixed /setupuser command --> changed to /newuser and changed ctx interaction command so that we can use slash commands 
        Fixed /horoscope command -->  changed ctx to interaction command so that we can use slash commands
            *Issues*
            - Need to throw in an if statement to handle the new users
            - Blocked out and left the old code in case something happens and so we can keep track of the commands we've changed to and interaction, we can delete and clean it up after we get done with our bot
4/23/26 Fixed /getuserinfo


# zodiac.py
4/15/26 removed, no longer needed - info is in the main.py

# Horoscope.sql --> Horoscope.sqlite
4/21/26 removed - we decided to not do this anymore

# fromapis.py
4/13/26 made code to get zodiac and the user's username to save to table in db
    *Issues*
    - When getting user_id, it gets by index number, but really want last inputs id + 1

# gitignore
4/22/26 Added discord.log, __pycache__, and .idea
