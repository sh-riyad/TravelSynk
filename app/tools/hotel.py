from app.schemas.Hotel import HotelInput
from langchain_core.tools import tool
from serpapi import GoogleSearch
from app.core.config import settings

@tool
def get_hotel_info(input_text: HotelInput) -> dict:
    """
    Retrieves hotel information based on user query using Google Hotels API via SerpAPI.
    """
    params = {**input_text.dict(), "api_key": settings.SERPAPI_API_KEY, "engine": "google_hotels"}
    search = GoogleSearch(params)
    return search.get_dict()