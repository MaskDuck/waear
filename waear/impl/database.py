from pymongo import MongoClient
from config import MONGODB_URL

class Database:
    def __init__(self):
        client = MongoClient(MONGODB_URL)
    
    async def add_allowed_server(self, server_id: int):
        database = client.core.servers
        database.insert_one({"_id": server_id, "type": "normal"})
    
    async def set_root_server(self, server_id: int):
        database = client.core.servers
        root_server = database.find_one({"type": "root"})
        if root_server:
            database.update_one({"type": "root"}, {"$set": {"_id": server_id}})
        else:
            database.insert_one({"_id": server_id, "type": "root"})