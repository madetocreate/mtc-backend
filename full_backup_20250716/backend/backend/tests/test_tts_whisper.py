import pytest
@pytest.mark.asyncio
async def test_tts_whisper():
    from services.tts_service import fake_tts
    from services.whisper_service import fake_whisper
    assert fake_tts() == "FAKE_AUDIO_DATA"
    assert await fake_whisper(b"x") == "Dies ist ein Dummy-Transkript."

