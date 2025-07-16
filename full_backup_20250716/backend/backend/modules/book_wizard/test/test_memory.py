def test_memory_save_and_read():
    from modules.book_wizard.creator_engine.modules.memory.memory_bridge import memory_save
    from modules.book_wizard.creator_engine.modules.memory.memory_bridge import read_memory

    memory_save("test", "Testinhalt", {"test_meta": True})
    mem = read_memory()
    assert "test" in mem
    assert any("Testinhalt" in entry.get("content", "") for entry in mem["test"])
