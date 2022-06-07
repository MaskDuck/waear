from nextcord.ext import tasks, commands


class AllowedServerManager(commands.Cog, command_attrs={"hidden": True}):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(minutes=30)
    async def autoleave(self):
        allowed_guilds = await self.bot.db.query_allowed_guilds()
        for guild in self.bot.guilds():
            if guild.id not in allowed_guilds:
                await guild.leave()

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        allowed_guilds = await self.bot.db.query_allowed_guilds()
        if guild.id not in allowed_guilds:
            await guild.leave()

    @commands.command()
    @commands.is_owner()
    async def allow_server(self, ctx, server_id: int):
        await ctx.db.add_allowed_server(server_id)
        await ctx.react(True)

    @commands.command()
    @commands.is_owner()
    async def set_root_server(self, ctx, server_id: int):
        await ctx.db.set_root(server_id)
        await ctx.react(True)


def setup(bot):
    bot.add_cog(AllowedServerManager(bot))
