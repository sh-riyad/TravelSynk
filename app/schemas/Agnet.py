from typing import Dict, Any

from pydantic import BaseModel

class AgentInput(BaseModel):
    """
    Pydantic model for validating input to the AgentCaller.
    """
    question: str

class AgentResponse(BaseModel):
    """
    Pydantic model for returning the complete response from the agent.
    Instead of just a string, it now supports a dictionary for full flexibility.
    """
    response: str