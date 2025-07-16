def test_memory_bulk():
    from services.memory_bulk import fake_memory_bulk
    result = fake_memory_bulk([1,2,3])
    assert result["count"] == 3

