def test_video():
    from services.video_service import fake_video
    assert fake_video("x") == "Fake video result"

