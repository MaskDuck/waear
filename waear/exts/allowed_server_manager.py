from nextcord.ext import tasks, commands
from typing import List
from typing_extensions import Self
from nextcord import Guild
from impl.context import Context


class AllowedServerManager(commands.Cog, command_attrs={"hidden": True}):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @tasks.loop(minutes=30)
    async def autoleave(self: Self):
        allowed_guilds: List[int] = await self.bot.db.query_allowed_guilds()
        for guild in self.bot.guilds():
            if guild.id not in allowed_guilds:
                await guild.leave()

    @commands.Cog.listener()
    async def on_guild_join(self: Self, guild: Guild) -> None:
        allowed_guilds: List[int] = await self.bot.db.query_allowed_guilds()
        if guild.id not in allowed_guilds:
            await guild.leave()

    @commands.command()
    @commands.is_owner()
    async def allow_server(self: Self, ctx: Context, server_id: int) -> None:
        await ctx.bot.db.add_allowed_server(server_id)
        await ctx.react(True)

    @commands.command()
    @commands.is_owner()
    async def set_root_server(self: Self, ctx: Context, server_id: int) -> None:
        await ctx.db.set_root_server(server_id)
        await ctx.react(True)


def setup(bot: commands.Bot):
    bot.add_cog(AllowedServerManager(bot))
