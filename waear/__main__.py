from nextcord.ext import commands
from nextcord import Intents, AllowedMentions
from impl.database import Database
from impl.context import Context
from logging import getLogger, INFO, StreamHandler
from config import BOT_TOKEN, OWNER_ID, ROOT_SERVER, COGS


from dotenv import load_dotenv

load_dotenv()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=Intents.all(),
            allowed_mentions=AllowedMentions(
                users=False, roles=False, replied_user=True, everyone=False
            ),
        )
        self.logger = getLogger("nextcord")
        self.logger.setLevel(INFO)
        self.logger.addHandler(StreamHandler())
        self.db = Database()
        self.db.set_initial_server(int(ROOT_SERVER))
        for cog in COGS:
            self.load_extension(cog)



    async def on_ready(self):
        self.logger.info("Bot successfully started")

    async def is_owner(self, user):
        return await super().is_owner(user) or (user.id == OWNER_ID)

    async def get_context(self, message, cls=Context):
        return await super().get_context(message, cls=cls)

    async def check_admin(self, interaction):
        admin_role = await self.db.get_admin_role(interaction.guild.id)
        return (
            await self.is_owner(interaction.user)
            or admin_role in [role.id for role in interaction.user.roles]
            or interaction.user.permissions.administrator
        )


bot = Bot()
bot.run(BOT_TOKEN)
