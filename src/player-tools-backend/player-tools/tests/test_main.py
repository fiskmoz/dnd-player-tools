""" Tests for endpoints """
from httpx import AsyncClient
import pytest


@pytest.mark.asyncio
async def test_healthcheck_async(async_client: AsyncClient):
    """ Test the healthcheck endpoint"""
    response = await async_client.get("/healthcheck")
    print(response)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
