""" Tests for endpoints """
import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_healthcheck_async(async_client: AsyncClient):
    """ Test the healthcheck endpoint"""
    response = await async_client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
