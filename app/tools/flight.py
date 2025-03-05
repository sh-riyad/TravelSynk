from app.core.config import settings
from app.schemas.Flight import FlightInput
from serpapi import GoogleSearch
from langchain_core.tools import tool

@tool
def get_flight_info(input_text: FlightInput) -> dict:
    """
    This tool retrieves flight information using the Google Flights API via SerpAPI.
    The function returns the JSON response as a dictionary.
    """
    params = {
        "engine": "google_flights",
        "departure_id": input_text.departure_id,
        "arrival_id": input_text.arrival_id,
        "outbound_date": input_text.outbound_date,
        "return_date": input_text.return_date,
        "currency": input_text.currency,
        "hl": input_text.hl,
        "api_key": settings.SERPAPI_API_KEY,
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results