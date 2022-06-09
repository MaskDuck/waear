from nextcord.ui import Modal, TextInput, View, button as ncbutton, Button
from nextcord import ButtonStyle, Interaction
from typing import Literal
from embeds.config import main_embed, authority_embed
from . import main_page


class RolePromptModal(Modal):
    def __init__(self, type: Literal["admin", "mod", "helper"], original_inter):
        super().__init__(title=f"Insert {type} Role ID", timeout=300.0)
        self.type = type
        self.id = TextInput(label="Role ID?")
        self.add_item(self.id)
        self.original_inter = original_inter

    async def interaction_check(self, interaction) -> bool:
        return interaction.client.check_admin(interaction)

    async def _verify_if_role_exist(self, interaction, role_id):
        try:
            result = interaction.guild.get_role(int(role_id))
        except ValueError:
            return False
        if not result:
            return False
        if result.id != int(role_id):
            return False
        return True

    async def callback(self, interaction):
        try:
            if (
                await self._verify_if_role_exist(
                    interaction, role_id=int(self.id.value)
                )
                is False
            ):
                await interaction.send(
                    "The role doesn't exist. Check the ID", ephemeral=True
                )
                return
        except ValueError:
            await interaction.send(
                "The role doesn't exist. Check the ID", ephemeral=True
            )
            return
        if self.type == "admin":
            await interaction.client.db.set_admin_role(
                interaction.guild.id, int(self.id.value)
            )
        if self.type == "mod":
            await interaction.client.db.set_mod_role(
                interaction.guild.id, int(self.id.value)
            )
        if self.type == "helper":
            await interaction.client.db.set_helper_role(
                interaction.guild.id, int(self.id.value)
            )
        admin_role = await interaction.client.db.get_admin_role(interaction.guild.id)
        mod_role = await interaction.client.db.get_mod_role(interaction.guild.id)
        helper_role = await interaction.client.db.get_helper_role(interaction.guild.id)
        await self.original_inter.edit_original_message(
            embed=authority_embed(
                admin_role=admin_role, mod_role=mod_role, helper_role=helper_role
            ),
        )


class AuthorityView(View):
    def __init__(self):
        super().__init__()

    @ncbutton(label="Edit admin role", style=ButtonStyle.success)
    async def _edit_admin_role_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.response.send_modal(RolePromptModal("admin", interaction))

    @ncbutton(label="Edit mod role", style=ButtonStyle.success)
    async def _edit_mod_role_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.response.send_modal(RolePromptModal("mod", interaction))

    @ncbutton(label="Edit helper role", style=ButtonStyle.success)
    async def _edit_helper_role_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.response.send_modal(RolePromptModal("helper", interaction))

    @ncbutton(label="Go home", style=ButtonStyle.secondary)
    async def _go_home_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.response.edit_message(
            embed=main_embed(), view=main_page.MainView()
        )
