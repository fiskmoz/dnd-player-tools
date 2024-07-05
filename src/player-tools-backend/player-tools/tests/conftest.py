""" Config for pytest """
from typing import  Generator
import asyncio
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from api.database.db import get_session_async
from api.database.models import CharacterSheet
from api.main import app
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:admin@test_db:5432"

@pytest.fixture(scope="session")
def test_database() -> AsyncSession:
    """ Creates a db connection session with rollback """
    async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
    async_session_local = async_sessionmaker(async_engine,   
        expire_on_commit=False,
        autoflush=False,
        autocommit=False,
        class_=AsyncSession
        )

    app.dependency_overrides[get_session_async] = lambda: async_session_local

    session_instance = async_session_local()

    yield session_instance

    session_instance.rollback()
    session_instance.close()

@pytest.fixture(scope="session")
def event_loop():
    """Overrides pytest default function scoped event loop"""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()

# Non async http client
@pytest.fixture()
def client() -> Generator:
    """ Get synchronous client """
    yield TestClient(app)


# Async http client
@pytest.fixture()
async def async_client() :
    """ Get async client"""
    async with AsyncClient(app=app, base_url="http://localhost:8000") as async_http_client:
        return  async_http_client

# testable character sheets
@pytest.fixture
async def testable_character_sheets(test_database: AsyncSession):
    """Creates some sheets for testing """
    test_sheet_1 = CharacterSheet(Name="Marcus")
    test_sheet_2 = CharacterSheet(Name="Johan")
    test_database.add(test_sheet_1)
    test_database.add(test_sheet_2)
    return [test_sheet_1, test_sheet_2]
