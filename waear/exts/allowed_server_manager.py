from nextcord.ext import tasks, commands

class AutoLeave(commands.Bot):
    def __init__(self, bot):
        self.bot = bot
    
    @tasks.loop(minutes=30)
    async def autoleave(self):
        ...
    
    @commands.command()
    @commands.is_owner()
    async def allow_server(self, ctx, server_id: int):
        await ctx.db.set_root_server(server_id)
        await ctx.send
