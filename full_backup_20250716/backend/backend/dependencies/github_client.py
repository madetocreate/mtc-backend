from github import Github
import os

github_token = os.getenv("GITHUB_TOKEN")
g = Github(github_token)
def get_github_client():
    return g
