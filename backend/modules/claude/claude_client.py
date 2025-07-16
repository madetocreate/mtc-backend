import os
from anthropic import Anthropic
claude_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
