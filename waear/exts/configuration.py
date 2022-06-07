from nextcord.ext import commands
from nextcord import slash_command

class Configuration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @slash_command()
    async def config(self, interaction):
        """Configure how the server should behave."""
        ...

    