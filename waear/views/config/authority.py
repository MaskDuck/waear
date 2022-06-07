from nextcord.ui import Modal, TextInput, View, button as ncbutton, Button
from nextcord import ButtonStyle, Interaction
from typing import Literal

class RolePromptModal(Modal):
    def __init__(self, type: Literal['admin', 'mod', 'helper']):
        super().__init__(title=f"Insert {type} Role ID", timeout=300.0)
        self.type = type
        self.id = TextInput(name="Role ID?", custom_id=f'ti:config.authority.{type}.id')
        self.add_item(self.id)
    
    async def interaction_check(self, interaction) -> bool:
        return interaction.client.check_admin(interaction)
    
    async def _verify_if_role_exist(self, interaction, role_id):
        return interaction.guild.get_role(role_id) != None
    
    async def callback(self, interaction):
        if not self._verify_if_role_exist:
            await interaction.send("The role doesn't exist. Check the ID", ephemeral=True)
        if self.type == "admin":
            await interaction.client.set_admin_role()
        await interaction.send("I set the {} role to <@&{}>.".format(self.type, self.id))

class AuthorityView(View):
    def __init__(self):
        ...
    
    @ncbutton(label="Edit admin role", style=ButtonStyle.success)
    async def _edit_admin_role_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.send_modal(RolePromptModal('admin'))
    
    @ncbutton(label="Edit mod role", style=ButtonStyle.success)
    async def _edit_mod_role_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.send_modal(RolePromptModal('mod'))
    
    @ncbutton(label="Edit helper role", style=ButtonStyle.success)
    async def _edit_mod_role_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.send_modal(RolePromptModal('helper'))
    
    @ncbutton(label="Go home", style=ButtonStyle.success)
    async def _go_home_callback(self, button: Button, interaction: Interaction):  # type: ignore
        await interaction.edit_original_message()
    
    
    


        