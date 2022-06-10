from nextcord import Embed, Colour
from typing import Union


def authority_embed(
    admin_role: Union[int, str] = None,
    mod_role: Union[int, str] = None,
    helper_role: Union[int, str] = None,
) -> Embed:
    return Embed(
        title="Authority",
        description=f"""
        This section allows you to manage role.
        You currently have these role setup:
        Admin role: <@&{admin_role}>
        Mod role: <@&{mod_role}>
        Helper role: <@&{helper_role}>""",
        colour=Colour.default(),
    )


def main_embed() -> Embed:
    return Embed(
        title="Welcome to the config.",
        description="Choose a section below by the dropdown to config.",
        colour=Colour.default(),
    )
