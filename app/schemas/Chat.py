from typing import Optional
from pydantic import BaseModel, ConfigDict

class ChatInput(BaseModel):
    thread_id: int
    message: str

# Define response schema (optional but recommended)
class ChatResponse(BaseModel):
    message: str
    thread_id: int
    response: str

    model_config = ConfigDict(from_attributes=True)

class StoreChatMessage(BaseModel):
    message_type: str
    content: str

class StoreMessageInput(BaseModel):
    user_id: int
    thread_id: int
    message_type: str
    content: str

    model_config = ConfigDict(from_attributes=True)


class ChatHistoryRequest(BaseModel):
    thread_id: Optional [int] = None
    skip: int = 0
    limit: int = 10

class ChatHistoryResponse(BaseModel):
    chat_history : list