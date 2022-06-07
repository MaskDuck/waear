from nextcord.ui import Select
from nextcord import SelectOption

class MainPageDropdown(Select):
    def __init__(self):
        options = [
            SelectOption(label='Authority', emoji="🔑", value="s:config.main.authority", description="Manage admin/mod/trusted/etc role"),
        ]
        super().__init__(custom_id="dd:config.main", options=options, placeholder="Select where you want to go...")  

    async def callback(self, interaction):
        if "s:config.main.authority" in self.values:
            ...
    