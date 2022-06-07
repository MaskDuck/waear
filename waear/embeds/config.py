from nextcord import Embed, Colour

def authority_embed(admin_role=None, mod_role=None, helper_role=None):
    return Embed(
        title = "Authority",
        description = f"""
        This section allows you to manage role.
        You currently have these role setup:
        Admin role: <@&{admin_role}>"""
    )