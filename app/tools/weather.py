import os
import requests
from langchain_core.tools import tool
from app.schemas.Weather import CityInput, CoordinatesInput, CityResponse, CoordinatesResponse
from app.core.config import settings

@tool
def get_city_lat_lon(input_text: CityInput) -> CoordinatesResponse:
    """
    Retrieves the latitude and longitude of a specified city using OpenWeather API.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={input_text.city},{input_text.country_code}&limit=1&appid={settings.OPENWEATHER_API_KEY}&mode=JSON"
    response = requests.get(url)
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return CoordinatesResponse(lat=data["lat"], lon=data["lon"])
    raise ValueError("City not found or invalid response from API")

@tool
def get_weather(input_text: CoordinatesInput) -> CityResponse:
    """
    Retrieves the current weather information for the given latitude and longitude using OpenWeather API.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={input_text.lat}&lon={input_text.lon}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200 and response.json():
        data = response.json()
        return CityResponse(weather_description=data["weather"][0]["description"])
    raise ValueError("Unable to retrieve weather data")
