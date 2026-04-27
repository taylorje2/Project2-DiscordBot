import discord
from discord import app_commands

# class 
def help(bot):
    @bot.tree.command(name="help", description="Show available commands")
    async def help(interaction: discord.Interaction):
        # lists embeds for all commands
        embed = discord.Embed(title="Bot Commands", description="Here are the available bot commands", color=discord.Color.pink())
        # embed for /newuser
        embed.add_field(name="/newuser", value="Create a new User", inline=False)
        # embed for /getuserinfo
        embed.add_field(name="/getuserinfo", value="view user information - username and zodiac sign", inline=False)
        # embed for /updateusername
        embed.add_field(name="/updateusername", value="update username", inline=False)
        # embed for /updateuserzodiac
        embed.add_field(name="/updateuserzodiac", value="update zodiac sign", inline=False)
        # embed for /delete
        embed.add_field(name="/delete", value="Delete user", inline=False)
        # embed for /horoscope
        embed.add_field(name="/horoscope", value="Get your daily horoscope", inline=False)
        # embed for /moon
        embed.add_field(name="/moon", value="Get Today's Moon Phase", inline=False)
        # embed for /apod
        embed.add_field(name="/apod", value="Get the NASA APOD for today", inline=False)
        # embed for /oldapod
        embed.add_field(name="/oldapod", value="Get the NASA APOD for a past date", inline=False)
        # embed for /help
        embed.add_field(name="/help", value="Create a new User", inline=False)
        # embed for tip
        embed.set_footer(text="Tip: Use /help to view commands anytime")

        return embed