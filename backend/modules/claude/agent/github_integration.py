from dotenv import load_dotenv
import os
from github import Github

# Lade die .env von exakt da, wo du willst:
load_dotenv(dotenv_path='../.env')

# Hole das Token aus der geladenen .env
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
print("TOKEN:", GITHUB_TOKEN)  # Optional, kannst du später auskommentieren

g = Github(GITHUB_TOKEN)
print("GitHub API ready")

def list_repos():
    for repo in g.get_user().get_repos():
        print(repo.full_name)
