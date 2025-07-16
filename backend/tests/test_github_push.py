import pytest
from services.github import push_to_github
def test_github_push(monkeypatch):
    def fake_push(repo_name, file_path, content, message):
        return True
    monkeypatch.setattr("services.github.push_to_github", fake_push)
    assert push_to_github("repo", "file", "data", "msg") == True
