from pydantic import BaseModel

class CompletionsRequest(BaseModel):
    message: str