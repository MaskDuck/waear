from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nextcord import Interaction
    from impl.database import Database

async def is_admin(interaction: Interaction) -> bool:
    database: Database = interaction.client.db
    admin_role_id: int = await database.get_admin_role(interaction.guild.id)
    return admin_role_id in [role.id for role in interaction.user.roles]

async def is_mod(interaction: Interaction) -> bool:
    database: Database = interaction.client.db 
    mod_role_id: int = await database.get_mod_role(interaction.guild.id)
    return mod_role_id in [role.id for role in interaction.user.roles]

async def is_helper(interaction: Interaction) -> bool:
    database: Database = interaction.client.db 
    helper_role_id: int = await database.get_helper_role(interaction.guild.id)
    return helper_role_id in [role.id for role in interaction.user.roles]