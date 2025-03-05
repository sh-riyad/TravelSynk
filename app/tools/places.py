from app.schemas.Places import PlacesInput
from serpapi import GoogleSearch
from langchain_core.tools import tool
from app.core.config import settings

@tool
def get_places_details(input_text: PlacesInput) -> dict:
    """
    This tool retrieves information about various places—such as restaurants, coffee shops, and cinema halls using the Google Places API.
    """
    params = {
        "q": input_text.query,
        "location": input_text.location,
        "hl": input_text.language_code,
        "gl": input_text.country_code,
        "api_key": settings.SERPAPI_API_KEY,
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results["local_results"]["places"]