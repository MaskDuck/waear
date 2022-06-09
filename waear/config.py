from os import getenv
from dotenv import load_dotenv

load_dotenv()


def _raisable_getenv(key, default=None, *, raise_if_none=False):
    output = getenv(key, default)
    if (not output) and (raise_if_none):
        raise KeyError("environment variable {} not found".format(key))
    return output


# bot stuff
COGS = ["exts.allowed_server_manager", "exts.configuration", "exts.owner"]

# required
BOT_TOKEN = _raisable_getenv("BOT_TOKEN", raise_if_none=True)
MONGODB_URL = _raisable_getenv("MONGODB_URL", raise_if_none=True)
ROOT_SERVER = _raisable_getenv("ROOT_SERVER")

# optional
OWNER_ID = _raisable_getenv("OWNER_ID")
CHECK_MARK = _raisable_getenv("CHECK_MARK", default="✅")
X_TICK = _raisable_getenv("X_TICK", default="❌")
