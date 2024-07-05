""" Setup for postgres DB """

from typing import AsyncIterator
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession, async_sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:admin@db:5432"

async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session_local = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_session_async() -> AsyncIterator[async_sessionmaker]:
    """" Get async session from pgsql """
    yield async_session_local()
