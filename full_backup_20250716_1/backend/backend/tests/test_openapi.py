def test_openapi():
    from services.openapi import fake_openapi
    assert "Dummy" in fake_openapi({})

