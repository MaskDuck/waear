from nextcord.ui import Select, View
from nextcord import SelectOption
from .authority import AuthorityView
from embeds.config import authority_embed

class MainPageDropdown(Select):
    def __init__(self):
        options = [
            SelectOption(label='Authority', emoji="🔑", value="s:config.main.authority", description="Manage admin/mod/trusted/etc role"),
        ]
        super().__init__(custom_id="dd:config.main", options=options, placeholder="Select where you want to go...")  

    async def callback(self, interaction):
        if "s:config.main.authority" in self.values:
            admin_role = await interaction.client.db.get_admin_role(interaction.guild.id)
            mod_role = await interaction.client.db.get_mod_role(interaction.guild.id)
            helper_role = await interaction.client.db.get_helper_role(interaction.guild.id)
            await interaction.edit_original_message(view=AuthorityView(), embed=authority_embed(admin_role=admin_role, mod_role=mod_role, helper_role=helper_role))

class MainView(View):
    def __init__(self):
        super().__init__()
        self.add_item(MainPageDropdown())
    

    