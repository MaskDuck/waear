from nextcord.ext import commands
from nextcord import Intents
from impl.database import Database
from impl.context import Context
from logging import getLogger, INFO, StreamHandler
from config import BOT_TOKEN, OWNER_ID, ROOT_SERVER, COGS


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=Intents.all())
        self.logger = getLogger("nextcord")
        self.logger.setLevel(INFO)
        self.logger.addHandler(StreamHandler())
        self.db = Database()
        self.db.set_root_server(int(ROOT_SERVER))
        for cog in COGS:
            self.load_extension(cog)

    async def on_ready(self):
        self.logger.info("Bot successfully started")

    async def is_owner(self, user):
        return super().is_owner(user) or (user.id == OWNER_ID)

    async def get_context(self, message, cls=Context):
        return await super().get_context(message, cls=cls)


bot = Bot()
bot.run(BOT_TOKEN)
