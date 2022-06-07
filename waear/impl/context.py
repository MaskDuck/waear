from nextcord.ext.commands import Context as _BaseContext
from config import CHECK_MARK, X_TICK


class Context(_BaseContext):
    def db(self):
        return self.bot.db

    def tick(self, state: bool):
        if state is True:
            return CHECK_MARK
        if state is None:
            return X_TICK
