from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base
from datetime import datetime


class History(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userid = Column(String, index=True)
    thread_id = Column(String, index=True)
    message_type = Column(String, index=True)
    content = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)