import pytest
from tests.conftest import client

from httpx import AsyncClient

def test_register():
    response = client.post("/user/", json={"name": "Beka", "password": "1234"})
    assert 200 == response.status_code


async def test_user_register(ac: AsyncClient):
    response = await ac.get("/users/")
    assert 200 == response.status_code
