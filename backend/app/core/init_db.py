from .db import engine, Base
from app.models.core import Tenant, App, Document

async def init_models():
    async with engine.begin() as conn:
        # Warning: This drops tables if they exist in dev mode!
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
