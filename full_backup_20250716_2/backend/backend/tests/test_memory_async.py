import pytest
from services.memory_service import save_memory, get_memory
import asyncio
@pytest.mark.asyncio
async def test_memory():
    await save_memory("test")
    memory = await get_memory()
    assert "test" in memory["memory"]
