def test_health_commit():
    from routers.health_commit import health_commit
    assert health_commit()["status"] == "commit-ok"

