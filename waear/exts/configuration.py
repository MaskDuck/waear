from nextcord.ext import commands
from nextcord import slash_command, Interaction, Role, SlashOption
from views.config.main_page import MainView
from embeds.config import main_embed
from typing_extensions import Self



class Configuration(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
    
    @slash_command()
    async def config(self: Self, interaction: Interaction) -> None:
        pass

    @config.subcommand()
    async def interactive(self: Self, interaction: Interaction) -> None:
        """Interactively configure how the server should behave."""
        await interaction.response.defer()
        await interaction.send(view=MainView(), embed=main_embed())
    
    @config.subcommand()
    async def authority(self: Self, interaction: Interaction) -> None:
        pass

    @authority.subcommand()
    async def admin_role(self: Self, interaction: Interaction, role: Role = SlashOption(name='admin_role', description='The admin role. People with admin perm always have this authority.')) -> None:
        """Set the admin role."""
        await interaction.client.db.set_admin_role(server_id=interaction.guild.id, role_id=role.id)
        await interaction.send("I set the admin role to {}".format(role.mention), ephemeral=True)
    
    @authority.subcommand()
    async def mod_role(self: Self, interaction: Interaction, role: Role = SlashOption(name='mod_role', description='The mod role. People with admin perm always have this authority.')) -> None:
        """Set the mod role."""
        await interaction.client.db.set_mod_role(server_id=interaction.guild.id, role_id=role.id)
        await interaction.send("I set the mod role to {}".format(role.mention), ephemeral=True)

    @authority.subcommand()
    async def helper_role(self: Self, interaction: Interaction, role: Role = SlashOption(name='helper_role', description='The helper role. People with admin perm always have this authority.')) -> None:
        """Set the helper role."""
        await interaction.client.db.set_helper_role(server_id=interaction.guild.id, role_id=role.id)
        await interaction.send("I set the helper role to {}".format(role.mention), ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(Configuration(bot))
