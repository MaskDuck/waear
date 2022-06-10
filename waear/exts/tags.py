from nextcord.ext import commands
from typing_extensions import Self
from nextcord import slash_command, Interaction


class Tags(commands.Cog):
    def __init__(self: Self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @slash_command()
    async def tag(self: Self, interaction: Interaction):
        pass