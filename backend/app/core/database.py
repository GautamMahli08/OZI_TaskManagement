from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class Database:
    client: AsyncIOMotorClient = None

db = Database()

async def get_database():
    return db.client[settings.DATABASE_NAME]

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(settings.DATABASE_URL)
    # Test connection
    await db.client.admin.command('ping')

async def close_mongo_connection():
    if db.client:
        db.client.close()

async def get_users_collection():
    database = await get_database()
    return database.users

async def get_tasks_collection():
    database = await get_database()
    return database.tasks