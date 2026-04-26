import discord
from discord import app_commands

class Confirm (discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="\u2705 Yes", style=discord.ButtonStyle.green)
    async def yes(self, interaction: discord.interactions, button: discord.ui.button):
        self.value = True
        self.stop()
        await interaction.response.defer()

    @discord.ui.button(label="\u274C No", style=discord.ButtonStyle.red)
    async def no(self, interaction: discord.interactions, button: discord.ui.button):
        self.value = False
        self.stop()
        await interaction.response.defer()







#-------------------------- Outside Resources --------------------------
# ui button -- https://discordpy.readthedocs.io/en/stable/interactions/api.html#discord.ui.Button.view
# ui button -- https://guide.pycord.dev/interactions/ui-components/buttons#:~:text=import%20discord,class%20that%20contains%20the%20button
# ui button -- https://stackoverflow.com/questions/79653645/how-to-make-a-confirmation-prompt-with-buttons-with-a-discord-bot-in-discord-py
# interaction response -- https://discordpy.readthedocs.io/en/latest/interactions/api.html#discord.InteractionResponse
# emoji unicode -- https://gist.github.com/chrisurf/a372d3e7de5371401b23217533a9476a