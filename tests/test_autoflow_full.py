def test_autoflow_runs():
    from creator_engine.modules.book_wizard.autogen.full_autoflow import run_full_autoflow
    result = run_full_autoflow("Testbuch", "neutral")
    assert isinstance(result, dict)
    assert len(result) > 0
