""" Setup for postgres DB """

from sqlalchemy.ext.asyncio import create_async_engine, async_session
from .models import Base



SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://user:password@postgresserver/db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
local_session = async_session(engine)


async def get_db_session_async():
    """Gets a db session"""
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all(bind=engine))
    database = local_session()
    try:
        yield database
    finally:
        await database.close()