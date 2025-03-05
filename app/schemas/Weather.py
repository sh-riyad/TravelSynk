from pydantic import BaseModel

class CityInput(BaseModel):
    """
    Pydantic model for validating input related to city and country code.
    """
    city: str
    country_code: str

class CityResponse(BaseModel):
    """
    Pydantic model for returning the response for city-based weather queries.
    The response is a string describing the weather.
    """
    weather_description: str  # Returns a descriptive weather summary

class CoordinatesInput(BaseModel):
    """
    Pydantic model for validating input related to latitude and longitude.
    """
    lat: float
    lon: float

class CoordinatesResponse(BaseModel):
    """
    Pydantic model for returning the response for coordinate-based weather queries.
    Returns only latitude and longitude values.
    """
    lat: float
    lon: float
