from sqlalchemy import asc
from sqlalchemy.orm import Session
from datetime import datetime
from app.models import History
from app.schemas.Chat import StoreMessageInput
from app.schemas.Chat import ChatHistoryRequest


def store_chat_message(input_text: StoreMessageInput, db: Session):
    """
    Inserts a chat message into the database.
    """
    db_chat = History(
        userid=input_text.user_id,
        thread_id=input_text.thread_id,
        message_type=input_text.message_type,
        content=input_text.content,
        timestamp=datetime.utcnow()
    )

    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)

    return db_chat



def get_chat_history(input_text: ChatHistoryRequest, user_id:int, db: Session):

    query = db.query(History).filter(History.userid == user_id)

    # Apply thread filtering if thread_id is provided
    if input_text.thread_id:
        query = query.filter(History.thread_id == input_text.thread_id)

    # Sort by thread_id and apply pagination
    chat_entries = query.order_by(asc(History.thread_id)).offset(input_text.skip).limit(input_text.limit).all()

    chat_entries = query.order_by(asc(History.thread_id)).offset(input_text.skip).limit(input_text.limit).all()

    formatted_chat_history = [
        {
            "thread_id": entry.thread_id,
            "message_type": entry.message_type,
            "content": entry.content,
            "timestamp": entry.timestamp
        }
        for entry in chat_entries
    ]

    return formatted_chat_history