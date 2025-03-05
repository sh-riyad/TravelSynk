from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
# The `check_same_thread=False` allows multiple threads to share the same connection

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
    Creates a session factory that generates new sessions for database interactions
    `autocommit=False` ensures transactions must be committed manually
    `autoflush=False` prevents automatic writing to the database before commit
"""

Base = declarative_base()

def init_db():
    from app.models import User, History
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()