import pytest
from services.chat_service import chat_service
@pytest.mark.asyncio
async def test_chat():
    result = await chat_service("hi")
    assert result == "Echo: hi"
