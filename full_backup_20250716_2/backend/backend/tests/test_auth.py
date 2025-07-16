def test_auth():
    from services.auth_service import fake_auth
    assert "Fake login" in fake_auth("user")

