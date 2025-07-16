import asyncio
from services.batch_commit import batch_commit

def github_batch_background(repo, files, author):
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, batch_commit, repo, files, author)
