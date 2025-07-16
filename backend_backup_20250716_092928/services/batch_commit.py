from services.github import commit_file

def batch_commit(repo_name, files, author):
    for f in files:
        commit_file(repo_name, f["path"], f["content"], "batch commit", author)
    return True
