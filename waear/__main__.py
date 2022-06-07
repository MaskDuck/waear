import nextcord
from nextcord.ext import commands
from nextcord import Intents
from impl.database import Database
from logging import getLogger, INFO, StreamHandler
from config import BOT_TOKEN, OWNER_ID, ROOT_SERVER
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=Intents.all())
        self.logger = getLogger("nextcord")
        self.logger.setLevel(INFO)
        self.logger.addHandler(StreamHandler())
        self.db.set_root_server(int(ROOT_SERVER))
    async def on_ready(self):
        self.logger.info("Bot successfully started")
    
    async def is_owner(self, user):
        return super().is_owner(user) or (user.id == USER_ID)
    
    
bot = Bot()
bot.run(BOT_TOKEN)
    
    