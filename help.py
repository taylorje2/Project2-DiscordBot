import discord

# embeded help menu
async def helpme(interaction: discord.Interaction):
    # lists embeds for all commands
    embed = discord.Embed(title="__**Help Menu**__", description="Here are the available bot commands", color=discord.Color.pink())

    # embed for /newuser
    embed.add_field(name="/newuser", value="Create a new User", inline=False)
    # embed for /getuserinfo
    embed.add_field(name="/getuserinfo", value="view user information - username and zodiac sign", inline=False)
    # embed for /updateusername
    embed.add_field(name="/updateusername", value="Update username", inline=False)
    # embed for /updateuserzodiac
    embed.add_field(name="/updateuserzodiac", value="Update zodiac sign", inline=False)
    # embed for /delete
    embed.add_field(name="/delete", value="Delete user", inline=False)

    # embed for /horoscope
    embed.add_field(name="/horoscope", value="Get your daily horoscope", inline=False)
    # embed for /moon
    embed.add_field(name="/moon", value="Get Today's Moon Phase", inline=False)
    # embed for /apod
    embed.add_field(name="/apod", value="Get the NASA APOD for today", inline=False)
    # embed for /oldapod
    embed.add_field(name="/oldapod", value="Get the NASA APOD for a past date\nDate format is YYYY-MM-DD\nPlease enter dashes (-) as well\nDatabase cannot go further than 1995-06-16", inline=False)
    
    # embed for /help
    embed.add_field(name="/help", value="Show all commands", inline=False)

    # embed for tip
    embed.set_footer(text="Use /help to view all commands anytime")
    
    await interaction.response.send_message(embed=embed)
