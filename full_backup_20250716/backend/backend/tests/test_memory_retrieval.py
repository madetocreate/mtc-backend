def test_memory_retrieval():
    from services.memory_retrieval import fake_memory_retrieval
    assert "Fake result" in fake_memory_retrieval("x")

