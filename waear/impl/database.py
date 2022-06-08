from pymongo import MongoClient
from config import MONGODB_URL


class Database:
    def __init__(self):
        self.client = MongoClient(MONGODB_URL)

    async def add_allowed_server(self, server_id: int):
        database = self.client.core.servers
        database.insert_one({"_id": server_id, "type": "normal"})

    async def set_root_server(self, server_id: int):
        database = self.client.core.servers
        root_server = database.find_one({"type": "root"})
        if root_server:
            database.update_one({"type": "root"}, {"$set": {"_id": server_id}})
        else:
            database.insert_one({"_id": server_id, "type": "root"})
    
    def set_initial_server(self, server_id: int):
        database = self.client.core.servers
        root_server = database.find_one({"type": "root"})
        if root_server:
            database.update_one({"type": "root"}, {"$set": {"_id": server_id}})
        else:
            database.insert_one({"_id": server_id, "type": "root"})

    async def query_allowed_guilds(self):
        database = self.client.core.servers
        return [x["_id"] for x in database.find()]
    
    async def set_admin_role(self, server_id: int, role_id: int):
        database = self.client[f'{server_id}'].config
        result = database.find_one({"_id": "admin_role"})
        if result is not None:
            database.update_one({"_id": "admin_role"}, {"$set": {"admin_role": role_id}})
        database.insert_one({"_id": "admin_role", "admin_role": role_id}) 
    
    async def set_mod_role(self, server_id: int, role_id: int):
        database = self.client[f'{server_id}'].config
        result = database.find_one({"_id": "mod_role"})
        if result is not None:
            database.update_one({"_id": "mod_role"}, {"$set": {"mod_role": role_id}})
        database.insert_one({"_id": "mod_role", "mod_role": role_id}) 
    
    async def set_helper_role(self, server_id: int, role_id: int):
        database = self.client[f'{server_id}'].config
        result = database.find_one({"_id": "helper_role"})
        if result is not None:
            database.update_one({"_id": "helper_role"}, {"$set": {"helper_role": role_id}})
        database.insert_one({"_id": "helper_role", "helper_role": role_id}) 
    

    
    async def get_admin_role(self, server_id: int):
        database = self.client[f'{server_id}'].config
        result = database.find_one({"_id": "admin_role"})
        try:
            return result['admin_role']
        except:
            return None
    
    async def get_mod_role(self, server_id: int):
        database = self.client[f'{server_id}'].config
        result = database.find_one({"_id": "mod_role"})
        try:
            return result['mod_role']
        except:
            return None
    
    async def get_helper_role(self, server_id: int):
        database = self.client[f'{server_id}'].config
        result = database.find_one({"_id": "helper_role"})
        try:
            return result['helper_role']
        except:
            return None