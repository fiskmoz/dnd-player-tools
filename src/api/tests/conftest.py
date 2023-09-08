""" Config for pytest """
from typing import AsyncGenerator, Generator
import asyncio
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from main import app


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
async def async_client() -> AsyncGenerator:
    """ Get async client"""
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        yield ac
