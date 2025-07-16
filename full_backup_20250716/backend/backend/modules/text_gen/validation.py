from pydantic import BaseModel, constr

class PromptRequest(BaseModel):
    prompt: constr(min_length=1, max_length=500)

