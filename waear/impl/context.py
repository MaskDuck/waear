from nextcord.ext.commands import Context as _BaseContext
from config import CHECK_MARK, X_TICK
from contextlib import suppress
from nextcord import HTTPException
from typing_extensions import Self


class Context(_BaseContext):
    def db(self: Self):
        return self.bot.db

    def tick(self: Self, state: bool):
        if state is True:
            return CHECK_MARK
        if state is None:
            return X_TICK

    async def react(self, state: bool):
        with suppress(HTTPException):
            await self.message.add_reaction(self.tick(state))
