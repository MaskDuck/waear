from nextcord.ui import Modal, TextInput, View, button as ncbutton, Button
from nextcord import ButtonStyle, Interaction
from typing import Literal
from embeds.config import main_embed
from . import main_page


class RolePromptModal(Modal):
    def __init__(self, type: Literal["admin", "mod", "helper"]):
        super().__init__(title=f"Insert {type} Role ID", timeout=300.0)
        self.type = type
        self.id = TextInput(label="Role ID?")
        self.add_item(self.id)

    async def interaction_check(self, interaction) -> bool:
        return interaction.client.check_admin(interaction)

    async def _verify_if_role_exist(self, interaction, role_id):
        return interaction.guild.get_role(role_id) is not None

    async def callback(self, interaction):
        if self._verify_if_role_exist == False:
            await interaction.send(
                "The role doesn't exist. Check the ID", ephemeral=True
            )
        if self.type == "admin":
            await interaction.client.db.set_admin_role(
                interaction.guild.id, int(self.id.value)
            )
        await interaction.send(
            "I set the {} role to <@&{}>.".format(self.type, self.id.value), ephemeral=True
        )
        admin_role = await interaction.client.db.get_admin_role(
                interaction.guild.id
            )
            mod_role = await interaction.client.db.get_mod_role(interaction.guild.id)
            helper_role = await interaction.client.db.get_helper_role(
                interaction.guild.id
            )
            await interaction.response.edit_message(
                view=AuthorityView(),
                embed=authority_embed(
                    admin_role=admin_role, mod_role=mod_role, helper_role=helper_role
                ),
            )
        
        

class AuthorityView(View):
    def __init__(self):
        super().__init__()

    @ncbutton(label="Edit admin role", style=ButtonStyle.success)
    async def _edit_admin_role_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.response.send_modal(RolePromptModal("admin"))

    @ncbutton(label="Edit mod role", style=ButtonStyle.success)
    async def _edit_mod_role_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.response.send_modal(RolePromptModal("mod"))

    @ncbutton(label="Edit helper role", style=ButtonStyle.success)
    async def _edit_helper_role_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.response.send_modal(RolePromptModal("helper"))

    @ncbutton(label="Go home", style=ButtonStyle.secondary)
    async def _go_home_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.response.edit_message(
            embed=main_embed(), view=main_page.MainView()
        )
