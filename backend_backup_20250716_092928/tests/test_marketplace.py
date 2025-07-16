def test_marketplace():
    from services.marketplace import fake_marketplace
    assert "Added" in fake_marketplace("item")

