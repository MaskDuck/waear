from nextcord.ext import commands
from impl.context import Context
from typing_extensions import Self

class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def load(self: Self, ctx: Context, ext: str):
        self.bot.load_extension(ext)
        await ctx.react(True)

    @commands.command()
    async def reload(self: Self, ctx: Context, ext: str):
        self.bot.unload_extension(ext)
        self.bot.load_extension(ext)
        await ctx.react(True)

    @commands.command()
    async def unload(self: Self, ctx: Context, ext: str):
        self.bot.unload_extension(ext)
        await ctx.react(True)


def setup(bot):
    bot.add_cog(Owner(bot))
