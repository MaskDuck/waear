from nextcord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx, ext):
        self.bot.load_extension(ext)
        await ctx.react(True)

    @commands.command()
    async def reload(self, ctx, ext):
        self.bot.unload_extension(ext)
        self.bot.load_extension(ext)
        await ctx.react(True)

    @commands.command()
    async def unload(self, ctx, ext):
        self.bot.unload_extension(ext)
        await ctx.react(True)


def setup(bot):
    bot.add_cog(Owner(bot))
