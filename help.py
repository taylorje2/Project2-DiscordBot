import discord
from discord import app_commands

def helpcommand(bot):
    @bot.tree.command(name="help", description="Show available commands")
    async def help(interaction: discord.Interaction):
        embed = discord.Embed(title="Bot Commands", description="Here are the available bot commands", color=discord.Color.pink())
        embed.add_field(name="/newuser", value="Create a new User", inline=False)
        embed.add_field(name="/getuserinfo", value="Create a new User", inline=False)
        embed.add_field(name="/updateusername", value="Create a new User", inline=False)
        embed.add_field(name="/updateuserzodiac", value="Create a new User", inline=False)
        embed.add_field(name="/delete", value="Create a new User", inline=False)
        embed.add_field(name="/horoscope", value="Create a new User", inline=False)
        embed.add_field(name="/moon", value="Create a new User", inline=False)
        embed.add_field(name="/apod", value="Create a new User", inline=False)
        embed.add_field(name="/oldapod", value="Create a new User", inline=False)
        embed.add_field(name="/help", value="Create a new User", inline=False)


#-------------------------- Outside Resources --------------------------
# https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=help#help-commands
# https://guide.pycord.dev/extensions/commands/help-command
# https://stackoverflow.com/questions/64092921/how-do-i-put-discord-py-help-command-in-an-embed