import discord
from discord import app_commands

def helpcommand(bot):
    @bot.tree.command(name="help", description="Show available commands")
    async def help(interaction: discord.Interaction):
        embed = discord.Embed(title="Bot Commands", description="Here are the available bot commands", color=discord.Color.pink())
        embed.add_field(name="/newuser", value="Create a new User", inline=False)
        embed.add_field(name="/getuserinfo", value="view user information - username and zodiac sign", inline=False)
        embed.add_field(name="/updateusername", value="update username", inline=False)
        embed.add_field(name="/updateuserzodiac", value="update zodiac sign", inline=False)
        embed.add_field(name="/delete", value="Delete user", inline=False)
        embed.add_field(name="/horoscope", value="Get your daily horoscope", inline=False)
        embed.add_field(name="/moon", value="Get Today's Moon Phase", inline=False)
        embed.add_field(name="/apod", value="Get the NASA APOD for today", inline=False)
        embed.add_field(name="/oldapod", value="Get the NASA APOD for a past date", inline=False)
        embed.add_field(name="/help", value="Create a new User", inline=False)
        
        embed.set_footer(text="Tip: Use /help to view commands anytime")

        await interaction.response.send_message(embed=embed, ephemeral=True)


#-------------------------- Outside Resources --------------------------
# https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=help#help-commands
# https://guide.pycord.dev/extensions/commands/help-command
# https://stackoverflow.com/questions/64092921/how-do-i-put-discord-py-help-command-in-an-embed
# https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html