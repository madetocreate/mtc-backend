def claude_git_commit(msg):
    import subprocess
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", msg])
    subprocess.run(["git", "push", "origin", "main"])
