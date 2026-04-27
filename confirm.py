import discord
from discord import app_commands

# class for confirmation button
class Confirm (discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    # button for "yes"
    @discord.ui.button(label="\u2705 Yes", style=discord.ButtonStyle.green)
    async def yes(self, interaction: discord.interactions, button: discord.ui.button):
        self.value = True
        # once button is clicked it can no longer be clicked
        self.stop()
        await interaction.response.defer()
    # button for "no"
    @discord.ui.button(label="\u274C No", style=discord.ButtonStyle.red)
    async def no(self, interaction: discord.interactions, button: discord.ui.button):
        self.value = False
        # once button is clicked it can no longer be clicked
        self.stop()
        await interaction.response.defer()
