import pytest
from routers.aion import aion_prompt
@pytest.mark.asyncio
async def test_aion_prompt():
    response = await aion_prompt("Ping")
    assert "response" in response
