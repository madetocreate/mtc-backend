def test_context():
    from services.context_service import fake_context
    assert "Fake context" in fake_context("data")

