from nextcord.ext import commands
from nextcord import slash_command, Interaction
from views.config.main_page import MainView
from embeds.config import main_embed
from typing_extensions import Self



class Configuration(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @slash_command()
    async def config(self: Self, interaction: Interaction):
        """Configure how the server should behave."""
        await interaction.response.defer()
        await interaction.send(view=MainView(), embed=main_embed())


def setup(bot: commands.Bot):
    bot.add_cog(Configuration(bot))
