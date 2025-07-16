import pytest
from services.tts_service import tts
import asyncio
@pytest.mark.asyncio
async def test_tts():
    audio = await tts("test")
    assert audio == "FAKE_AUDIO_DATA"
