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
