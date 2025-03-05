from pydantic import BaseModel, HttpUrl
from typing import List

class NewsInput(BaseModel):
    message: str

class NewsArticle(BaseModel):
    """Represents a single news article with a title and URL."""
    title: str
    url: HttpUrl  # Ensures valid URL format

class NewsResponse(BaseModel):
    """Represents the structured response for fetching news."""
    status: str  # "ok" or "failed"
    news: List[NewsArticle]  # List of news articles