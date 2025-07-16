from modules.claude.claude_runner import run_claude_prompt
def aion_team_prompt(task):
 return run_claude_prompt(task)
from modules.claude.research.claude_research_bot import research_topic
def team_deep_search(query): return research_topic(query)
# Claude ist nun Research-Mitglied bei AION
