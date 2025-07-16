def test_voice():
    from services.voice_service import fake_voice
    assert fake_voice("test") == "FAKE_VOICE_DATA"

