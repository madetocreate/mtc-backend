from services.github import fake_github_push

def test_github_push():
    result = fake_github_push({"data": "test"})
    assert "Dummy push" in result

