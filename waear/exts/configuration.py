from nextcord.ext import commands
from nextcord import slash_command
from views.config.main_page import MainView
from embeds.config import main_embed

class Configuration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command()
    async def config(self, interaction):
        """Configure how the server should behave."""
        await interaction.response.defer()
        await interaction.send(view=MainView(), embed=main_embed())

def setup(bot):
    bot.add_cog(Configuration(bot))
        

    