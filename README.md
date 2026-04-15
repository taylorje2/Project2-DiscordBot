# Project 2 - Discord Bot
Moon/Horoscope/APOD
Repo for Project 2

# main.py
4/13/26 Made env file complete with token

# zodiac.py
4/9/26 started... buttttt... seeing if making the database would be easier....

# Horoscope.sql --> Horoscope.sqlite
4/9/26 started sql file to implement our horoscopes database - which will hold user DOB, zodiac signs, and daily horoscopes for each sign...
4/14/26 Removed and started a smaller sqlite file that auto increments/assigns userId that holds a users zodiac sign

# fromapis.py
4/13/26 made code to get zodiac and the user's username to save to table in db
    *Issues*
    - When getting user_id, it gets by index number, but really want last inputs id + 1
