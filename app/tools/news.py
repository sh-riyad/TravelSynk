from langchain_core.tools import tool
# from currentsapi import CurrentsAPI
from app.core.config import settings
from app.schemas.News import NewsInput, NewsResponse, NewsArticle


@tool
def get_current_news(input_text: NewsInput) -> NewsResponse:
    """
    Fetches the latest news articles based on the provided keyword using CurrentsAPI.
    """
    # api_key = settings.CURRENTS_API_KEY
    # currents_api = CurrentsAPI(api_key=settings.CURRENTS_API_KEY)
    # response = currents_api.search(keywords=input_text.message)
    #
    # if response["status"] == "ok":
    #     articles = [
    #         NewsArticle(title=article["title"], url=article["url"])
    #         for article in response["news"]
    #     ]
    #     return NewsResponse(status="ok", news=articles)

    return NewsResponse(status="failed", news=[])

