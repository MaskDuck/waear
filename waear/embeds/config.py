from nextcord import Embed, Colour

def authority_embed(admin_role=None, mod_role=None, helper_role=None):
    return Embed(
        title = "Authority",
        description = f"""
        This section allows you to manage role.
        You currently have these role setup:
        Admin role: <@&{admin_role}>
        Mod role: <@&{mod_role}>
        Helper role: <@&{helper_role}>""",
        colour=Colour.default()
    )

def main_embed():
    return Embed(
        title = "Welcome to the config.",
        description = "Choose a section below by the dropdown to config.",
        colour=Colour.default()
    )